""" Файл в котором описаны события """

from PySide6.QtWidgets import  QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Slot, QUrl, QTimer
import cv2
from ultralytics import YOLO
from qimage2ndarray import array2qimage
from threading import Thread, Condition



pauseFlag = False
condition = Condition()

@Slot()
def openFile(parent):
    options = QFileDialog.Options()
    fileName, _ = QFileDialog.getOpenFileName(parent, options=options)
    if fileName:
        parent.setText(fileName)


@Slot()
def startVideo(parent, modelName, fileName = None):
    global cap, timerFps
    model = YOLO(modelName)
    cap = cv2.VideoCapture(fileName)
    if not cap.isOpened():
        print("Ошибка открытия видео файла")
        return
    timerFps = QTimer()
    timerFps.start(25)
    timerFps.timeout.connect(lambda: Thread(target = postVideo(parent, model, cap)).start())
    

def preparationArray(parent, array):
    results =  parent.predict(array, verbose = False)
    array =cv2.resize(results[0].plot(), (661, 471), interpolation=cv2.INTER_AREA)
    return array


def ndarray2qpixmap(array):
    array = array2qimage(array)
    pixArray = QPixmap.fromImage(array)
    return pixArray


@Slot()
def postVideo(parent, model, capture):
    inspectFlag()
    inf, array = capture.read()
    if not inf:
        cap.release()
        timerFps.stop()
        return
    array = preparationArray(model, cv2.cvtColor(array, cv2.COLOR_BGR2RGB))
    pixArray = ndarray2qpixmap(array)
    parent.setPixmap(pixArray)


def inspectFlag():
    global condition, pauseFlag
    if not pauseFlag:
        return  # Ожидаем изменение условия
    condition.wait()


@Slot()
def pauseVideo():
    global pauseFlag
    pauseFlag = True


@Slot()
def resumeVideo():
    global pauseFlag, condition
    pauseFlag = False
    with condition:
        # Уведомляем все ожидающие потоки об изменении условия
        condition.notify_all()

