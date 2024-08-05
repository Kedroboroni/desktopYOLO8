""" 
Файл в котором, размещены кнопки,
указанны ссылки на собития и указаны
ссылки на стили 
"""

from widgets import Lable, Button, GroupBox, LineEdit, Widget
from PySide6.QtWidgets import QMainWindow
from events import openFile, startVideo, pauseVideo, resumeVideo
from multiprocessing import Process

nameWeights = "best.pt"

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        """Размещаем свои виджеты"""
        centralWidget = Widget() #Создали центарльный виджет в котором будут располагаться другие виджеты
        self.setCentralWidget(centralWidget) #Разместили центральныйтвиджет в главном окне

        self.setStyleSheet("background-color:qconicalgradient(cx:0, cy:0, angle:135, stop:0.0454545 rgba(188, 55, 255, 144), stop:0.164773 rgba(80, 4, 197, 146), stop:0.272727 rgba(75, 46, 213, 162), stop:0.369318 rgba(162, 36, 251, 175), stop:0.494318 rgba(185, 98, 237, 175), stop:0.590909 rgba(231, 69, 222, 130), stop:0.698864 rgba(209, 36, 185, 188), stop:0.789773 rgba(189, 0, 122, 140), stop:0.897727 rgba(107, 10, 204, 153), stop:1 rgba(100, 0, 219, 157));\n"
                            "font: 10pt \"Noto Serif\";")

        """Создали компоненты которые распологаются в центральном виджете"""
        

        GroupBoxMousePosition = GroupBox(centralWidget, x = 20, y = 525, w = 318, h = 40) #Создали коробку для лебла, который выводит координаты\
        LineEditX = LineEdit(GroupBoxMousePosition, x = 4, y = 4, w = 153, h = 32)
        LineEditY = LineEdit(GroupBoxMousePosition, x = 160, y = 4, w = 153, h = 32)

        LableStream = Lable(centralWidget, mouseX = LineEditX, mouseY = LineEditY, x = 20, y = 10, w =661, h = 471) #Создали лебл просмотра кадров



        GroupBoxMangeVideo = GroupBox(centralWidget, x = 20, y = 490, w = 318, h = 30) #Создали коробку для кнопок паузы, и возабновления

        ButtonPause = Button(GroupBoxMangeVideo, text = "pause", x = 4, y = 4, w = 96, h = 22)
        ButtonPause.clicked.connect(pauseVideo)

        ButtonResume = Button(GroupBoxMangeVideo, text = "resume", x = 104, y = 4, w = 96, h = 22)
        ButtonResume.clicked.connect(resumeVideo)



        GroupBoxSettings = GroupBox(centralWidget, x = 700, y = 10, w = 201, h = 471) #Создали коробку для размещения виджетов настроек



        GroupBoxChange = GroupBox(centralWidget, x = 20, y = 570, w = 661, h = 30) #Создали коробку для размещения опций выбора источника потока/изображения/видео

        ButtonChange = Button(GroupBoxChange, text = "Change", x = 4, y = 4, w = 96, h = 22) #Создали кнопку выбора
        ButtonChange.clicked.connect(lambda: openFile(LineEditPath))

        ButtonOpen = Button(GroupBoxChange, text = "Open", x = 559, y = 4, w = 96, h = 22) #Создали кнопку открытия
        ButtonOpen.clicked.connect(lambda: startVideo(LableStream, nameWeights, LineEditPath.text()))

        LineEditPath= LineEdit(GroupBoxChange, x = 106, y = 4, w = 449, h = 22) #Создали строку ввода (вводится автоматически при выобре пути, через кнопку Change или можно ввести вручную и нажать кнопуку Open)



        ButtonClose = Button(centralWidget, text = "Close", x = 700, y = 570, w = 201, h = 30) #Создали кнопку закрытия
        ButtonClose.clicked.connect(self.close) #Закрываем приложение
    
""" @Slot()
    def runVideoThreding(self):
        self.threadVideo =videoThread(nameWeights, self.LineEditPath.text())
        self.threadVideo.pixmapSignal.connect(lambda: startVideo(self.LableStream, modelName, self.LineEditPath.text()))
        self.threadVideo.start()"""