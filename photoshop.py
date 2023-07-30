from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel,QPushButton,QWidget,QGridLayout
from PyQt6.QtGui import QIcon
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
        layout = QGridLayout()

        layout.addWidget(ButtonFerramenta(icone_criar_arquivo,"Criar Arquivo"), 0, 0)
        layout.addWidget(ButtonFerramenta(icone_importar_arquivo,"Importar Arquivo"), 1, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setLayout(layout)
        self.setCentralWidget(widget)



class PhotoshopPy(QMainWindow):
    def __init__(self,title_window:str,width:int,heigth:int) -> None:
        super().__init__()
        self.setWindowTitle(title_window)
        self.setGeometry(0,0,width,heigth)

    def functions_barras(self,text):
        btn = QPushButton(text)
        btn.setFixedSize(50,50)
        btn.move(100,75)

        return btn



if __name__ == "__main__":
    app = QApplication([])
    
    window = PhotoshopPy("Photoshop Python",800,600)
    ferramentas = BarraFerramentas()
    window.show()
    ferramentas.show()

    app.exec()

