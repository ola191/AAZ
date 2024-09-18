from PySide6.QtWidgets import QPushButton

class CustomButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(150, 40)
        self.setStyleSheet("font-size: 16px;")
