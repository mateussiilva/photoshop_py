from PIL import Image
import warnings
import cv2



Image.MAX_IMAGE_PIXELS = None


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

    def open_image_cv2(self,mostrar_img=False):
        i = cv2.imread(self.path_imagem)
        if mostrar_img:
            cv2.imshow(" ",i)
            while True:
                ...
        return i
    def show_image(self):
        i = self.__imagem
        # thub = i.thumbnail((100,100))
        return i.show()



if __name__ == "__main__":
    caminho = "media/mateus/ARQUIVOS/PAINEESI"
    p_imagem = "fundo1.tif"
    image = Imagem(p_imagem)
    img= image.open_image_cv2(True)
    # cv2.imshow("teste",img)
    

    