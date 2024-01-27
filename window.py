from PySide6.QtWidgets import (
    QWidget, QSlider, QLineEdit, QLabel,
    QPushButton, QScrollArea, QApplication,
    QHBoxLayout, QVBoxLayout, QMainWindow)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6 import QtWidgets
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Scroll Area which contains the widgets, set as the centralWidget
        self.scroll = QScrollArea()
        # Widget that contains the collection of Vertical Box
        self.widget = QWidget()
        # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.vbox = QVBoxLayout()

        self.lbl_image = QLabel("")
        self.bnt_get_image = QPushButton("Selecionar Imagem")
        self.bnt_get_image.clicked.connect(self.setar_imagem)
        self.vbox.addWidget(self.lbl_image)
        self.vbox.addWidget(self.bnt_get_image)

        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(0, 0, 800, 700)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

    def setar_imagem(self):
        pathimage = "background_police.jpg"
        image = QPixmap(pathimage)
        self.lbl_image.setPixmap(image)
        print("Hello")


app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
sys.exit(app.exec())
