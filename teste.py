import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QGridLayout, QWidget, QLabel, QScrollArea, QScrollBar
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Exemplo de QScrollArea')
        self.setGeometry(100, 100, 400, 300)

        # Criando o widget que será colocado na área de rolagem
        widget_content = QWidget()

        # Layout vertical para o widget_content
        layout = QVBoxLayout()

        # Adicionando vários widgets (labels) ao layout
        pixmap = QPixmap("fundo1.jpg")
        image_lbl = QLabel("")
        image_lbl.setPixmap(pixmap)

        # Definindo o layout para o widget_content
        layout.addWidget(image_lbl)
        widget_content.setLayout(layout)

        # Criando a área de rolagem e adicionando o widget_content a ela
        scroll_area = QScrollArea()
        scroll_area.setWidget(widget_content)

        # Criando barras de rolagem vertical e horizontal
        vertical_scrollbar = QScrollBar()
        horizontal_scrollbar = QScrollBar()

        # Configurando as barras de rolagem
        scroll_area.setVerticalScrollBar(vertical_scrollbar)
        scroll_area.setHorizontalScrollBar(horizontal_scrollbar)

        # Definindo a área de rolagem como widget central da janela principal
        self.setCentralWidget(scroll_area)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())