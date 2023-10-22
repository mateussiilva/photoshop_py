from PIL import Image
from os.path import getsize
import pprint 




class Imagem:
    def __init__(self,path_imagem) -> None:
        self.path_imagem = path_imagem
        self.__imagem = self.open_image_pillow(path_imagem)

    def open_image_pillow(self,path_image):
        try:
            img = Image.open(path_image) 
        except: 
            print("Error")
        return img

    def show_image(self):
        i = self.__imagem
        return i.show()
    
    def __get_size(self) -> tuple:
        size = self.__imagem.size
        return size
    
    def __get_resolution(self) -> tuple:
        dpi = self.__imagem.info["dpi"]
        return dpi

    def __get_size_image(self):
        size_file = getsize(self.path_imagem) 
        return (round(size_file / 1024 ** 2,3),"MB")

    def get_characteristics_for_image(self) -> dict:
        return {
            "tamanho_pixel": self.__get_size(),
            "resolução_dpi":self.__get_resolution(),
            "tamanho_arquivo": self.__get_size_image()
        }
        ...

def main():
    caminho = "media/mateus/ARQUIVOS/PAINEESI"
    p_imagem = "fundo1.jpg"
    image = Imagem(p_imagem)
    pprint.pprint(image.get_characteristics_for_image())


if __name__ == "__main__":
    Image.MAX_IMAGE_PIXELS = None # ME PERMITE ESTRAPOLAR O LIMITE DEFINIDO PELO PILLOW !!CUIDADO
    main()
    
    