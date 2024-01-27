
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout







class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PhotoPy")
        layout = QVBoxLayout()

        self.lbl_image = QLabel()
        self.bnt_get_image = QPushButton("Selecionar Imagem")
        self.bnt_get_image.clicked.connect(self.setar_imagem)
        
        layout.addWidget(self.lbl_image)
        layout.addWidget(self.bnt_get_image)
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
        
    def setar_imagem(self):
        pathimage = "background_police.jpg"
        image = QPixmap(pathimage)
        self.lbl_image.setPixmap(image)
        print("Hello")




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
