from PyQt6.QtWidgets import (
    QApplication,QMainWindow,QLabel,
    QPushButton,QWidget,QToolBar,QScrollArea,QScrollBar,QVBoxLayout,)
from PyQt6.QtGui import QAction, QIcon,QPixmap
from PySimpleGUIQt import popup_get_file

icone_criar_arquivo = "imagens/icons/icons8-crie-um-novo-16.png"
icone_importar_arquivo = "imagens/icons/icons8-import-file-16.png"

class ButtonFerramenta(QPushButton):
    def __init__(self,filename,action) -> None:
        super().__init__()
        self.action = action
        # self.setText(text)
        self.setIcon(QIcon(filename))
        self.setFixedSize(50,50)
        self.clicked.connect(self.clique)

    def clique(self):
        print(f"Você clicou {self.action}")
        


class BarraFerramentas(QMainWindow):
    def __init__(self):
        super().__init__()
        toolbar = QToolBar("Barra de ferramentas")
        self.addToolBar(toolbar)
        button_action = QAction("Your button", self)
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)



class PhotoshopPy(QMainWindow):
    def __init__(self,title_window:str,width:int,heigth:int) -> None:
        super().__init__()
        self.setWindowTitle(title_window)
        self.setGeometry(0,0,width,heigth)
        self.initUI()
        # DEFINIÇÃO DOS WIDGETS
        # layout = QVBoxLayout()
        # toolbar = QToolBar("Barra de ferramentas")
        # scroll_area = QScrollArea()
        # widget_content = QWidget()
        # vertical_scrollbar = QScrollBar()
        # horizontal_scrollbar = QScrollBar()
        # button_action = QAction("Abrir Arquivo",self)
        
        # button_action.triggered.connect(self.select_file)
        # pixmap = QPixmap("fundo1.jpg")
        # image_lbl = QLabel("")
        # image_lbl.setPixmap(pixmap)

        

        # # CONFIGURANDO OS WIDGETS
        # toolbar.addAction(button_action)

        # scroll_area.setWidget(widget_content)
        # scroll_area.setVerticalScrollBar(vertical_scrollbar)
        # scroll_area.setHorizontalScrollBar(horizontal_scrollbar)       
        
        # layout.addWidget(image_lbl)
        # widget_content.setLayout(layout)


        # self.addToolBar(toolbar) 
        # self.setCentralWidget(scroll_area)

    def initUI(self):
        self.setWindowTitle('Exemplo de QScrollArea')
        self.setGeometry(100, 100, 800, 600)

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
    
    def select_file(self):
        path_file = popup_get_file("Selecione o arquivo")
        return path_file

    def set_image(self):
        p_arquivo = self.select_file()

    



if __name__ == "__main__":
    app = QApplication([])
    
    window = PhotoshopPy("Photoshop Python",800,600)
    # ferramentas = BarraFerramentas()
    window.show()
    # ferramentas.show()

    app.exec()

