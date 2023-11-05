from PySimpleGUI import Window,WIN_CLOSED,Text,Input,FileBrowse,Multiline,Button
from PIL import Image


SIZE = 600,600
REZIBLE_SIZE  = tuple(map(lambda n: n*3,SIZE))
layout = [
    [Text("Selecione uma imagem:"),Input(key="-PATH_IMAGE-"),FileBrowse("Select Image",initial_folder="/home/mateus/Imagens/")],
    [Multiline(size=(100,30))],
    [Button("Dados da Imagem",key="-PEGAR_DADOS_IMAGE-")]
]



window = Window("Dados da imagem",layout,size=SIZE,resizable=REZIBLE_SIZE)

while True:
    events, values = window.read()
    
    if events == "-PEGAR_DADOS_IMAGE-":
        path_image = values["-PATH_IMAGE-"] 
        path_image = values["-PATH_IMAGE-"] if len(path_image) else "/home/mateus/Imagens/icone_python.png"
    if events == WIN_CLOSED:
        break
    
    
window.close()