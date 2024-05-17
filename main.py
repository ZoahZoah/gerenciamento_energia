# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from QrcFiles.ui_main_window import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        titulo_janela = 'Blink'

        self.ui = Ui_Widget()   
        self.ui.setupUi(self)               # set widget setup
        self.setWindowTitle(titulo_janela)  # set window title


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
