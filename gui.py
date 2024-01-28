import PySimpleGUI as sg
from photoshop import PhotoPy

layout = [
    [
        sg.Text("Imagem:"), sg.Input(key="-PATH_IMAGE-"),
        sg.FileBrowse("Open Image",key="-FILE_OPEN-")],
    [sg.Button("Load Image",key="-LOAD-")],
    [sg.Text(key="-RES-")]
]


window = sg.Window("PhotoPy", layout)
photopy = PhotoPy()
while 1:
    events, values = window.read()
    if events == "-LOAD-":
        image = values["-PATH_IMAGE-"]
        dados = photopy.dados_imagem(photopy.open_image(image))
        window["-RES-"].update(dados)
    if events == sg.WINDOW_CLOSED:
        break


window.close()
