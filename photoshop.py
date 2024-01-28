from PIL import Image
from os.path import join
import rembg


Image.MAX_IMAGE_PIXELS = None


class PhotoPy:
    def __init__(self) -> None:
        self.mode = "RGB"
        self.font_global = ""
        self.font_size = 48
    
    @classmethod
    def open_image(cls, filename: str, isgray: bool = False) -> Image:

        if isgray:
            img = Image.open(filename)
            return img.convert("L")

        img = Image.open(filename)
        return img

    def criar_image(self, name: str, size: tuple, color: tuple = (255,255,255), extensao: str = ".jpg"):
        i = Image.new(self.mode, size=size,color=color)
        p = name + extensao
        i.save(p)

    def size_image(self,img:Image) -> tuple:
        return img.size
        # return dict(zip(("w","h"),img.size))
    
    def dados_imagem(self,img):
        msg = f"""
        DPI: {self.get_dpi(img)}
        Dimensoes(PX): {self.size_image(img)}
        """
        # print(f"SIZE{}")
        print(msg)
        return msg
    
    @staticmethod    
    def get_dpi(img):
        try:
            return img.info["dpi"][0]
        except:
            return None
    # def save():
        

if __name__ == "__main__":
    photopy = PhotoPy()
    image = photopy.open_image(
        "images_teste/wide-angle-shot-two-women-walking-beach-with-surfing-boards.jpg", isgray=False)
    # image.show()
    image_sem_fundo = rembg.remove(image)

    image_sem_fundo.save("sem_fundo.png")
