from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget
from configs.configLoader import loadConfig

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.windowConfig = loadConfig("configs/window.json")
        self.windowSize = self.windowConfig["windowsSize"]

        self.setWindowTitle("AAZ")
        self.setGeometry(*self.windowSize)
        self.setContentsMargins(0, 0, 0, 0)

        self.setupUi()

    def setupUi(self):
        centralWidget = QWidget()
        mainLayout = QHBoxLayout()

        menu = QListWidget()
        menu.addItem("Dashboard")
        menu.addItem("Zadania")
        menu.addItem("Ustawienia")
        menu.setMinimumWidth(200)

        contentWidget = QWidget()
        contentLayout = QVBoxLayout()
        contentWidget.setLayout(contentLayout)

        mainLayout.addWidget(menu, 1) 
        mainLayout.addWidget(contentWidget, 4) 

        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)