from PySide6.QtWidgets import QApplication, QWidget
from form import Ui_Widget
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()  # Instancie a classe gerada pelo Qt Designer
        self.ui.setupUi(self)  # Configure a interface de usuário na janela principal



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sapp.exec()