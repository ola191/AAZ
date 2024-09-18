import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from styles import apply_styles
from ui_main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    apply_styles(app)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()