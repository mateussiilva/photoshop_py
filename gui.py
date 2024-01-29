import PySimpleGUI as sg
from PySimpleGUI import Text, Checkbox, Radio
from photoshop import PhotoPy

SIZE = 940, 800

frame_dados_imagem = [
    [Text(key="-RES-")]
]

layout = [
    [
        sg.Text("Imagem:"), sg.Input(key="-PATH_IMAGE-"),
        sg.FileBrowse("Open Image", key="-FILE_OPEN-"),
        sg.Button("Load Image", key="-LOAD-"),
    ],
    [sg.Frame(title="Dados Imagem",layout=frame_dados_imagem)]
]


window = sg.Window("PhotoPy", layout, size=SIZE)
photopy = PhotoPy()
while 1:
    # Ler os eventos e os valores da JANELA
    events, values = window.read()

    # Carregar a imagem e suas informações
    if events == "-LOAD-" or events == "-FILE_OPEN-":
        pathimage = values["-PATH_IMAGE-"]
        image = photopy.open_image(pathimage)
        dados = photopy.dados_imagem(image)
        window["-RES-"].update(dados)
        
    

        
    # Fechar a Janela 
    if events == sg.WINDOW_CLOSED:
        break


window.close()
