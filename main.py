import cv2
from PIL import Image



def get_size(filename):
    img = Image.open(filename)
    return img.size



class Imagem:
    def __init__(self,caminho_imagen) -> None:
        self.caminho_img = caminho_imagen
        self.imagem = Imagem.abrir_imagem(path_img=self.caminho_img)

    @staticmethod
    def abrir_imagem(path_img):
        try:
            img = Image.open(path_img)
        except:
            return None
        return img
    
    def get_dimensions(self) -> tuple:
        if self.imagem is not None:
            i = self.imagem.size
            return Imagem.converter_px_para_cm(i)

    def get_dpi(self):
        if self.imagem is not None:
        
            return self.imagem.info["dpi"][0]
    
    @staticmethod
    def converter_px_para_cm(dimensoes:tuple) -> tuple:
        return (
            float(dimensoes[0] * 0.0264583333),
            (float(dimensoes[1]) * 0.0264583333)
        )





if __name__ == "__main__":
    caminho_imagem = "fundo2.jpg"
    imagem = Imagem(caminho_imagem)
    
    # print(imagem.abrir_imagem(caminho_imagem))
    print(imagem.get_dimensions())
    print(imagem.get_dpi())