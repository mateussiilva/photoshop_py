import PySimpleGUI as sg
from photoshop import PhotoPy

SIZE = 940, 800

layout = [
    [
        sg.Text("Imagem:"), sg.Input(key="-PATH_IMAGE-"),
        sg.FileBrowse("Open Image", key="-FILE_OPEN-")
    ],
    [
        sg.Button("Load Image", key="-LOAD-")
    ],
    [sg.Text(key="-RES-")]
]


window = sg.Window("PhotoPy", layout, size=SIZE)
photopy = PhotoPy()
while 1:
    events, values = window.read()
    if events == "-LOAD-":
        pathimage = values["-PATH_IMAGE-"]
        image = photopy.open_image(pathimage)
        dados = photopy.dados_imagem(image)
        window["-RES-"].update(dados)
    if events == sg.WINDOW_CLOSED:
        break


window.close()
