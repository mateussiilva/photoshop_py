from PIL import Image
from rembg import remove
from math import ceil,floor


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

    def criar_image(self, name: str, size: tuple, color: tuple = (255, 255, 255), extensao: str = ".jpg"):
        i = Image.new(self.mode, size=size, color=color)
        p = name + extensao
        i.save(p)


    def size_image(self, img: Image, cm: bool = False) -> tuple:
        if cm:
            d = self.get_dpi(img) if self.get_dpi(img) is not None else 1

            return tuple(map(lambda x: floor( x / d * 2.54), img.size))

        return img.size


    def dados_imagem(self, img):
        msg = f"""
        DPI: {self.get_dpi(img)}
        Dimensoes(PX): {self.size_image(img)}
        Dimensoes(CM): {self.size_image(img,cm=True)}
        """
        # print(f"SIZE{}")
        print(msg)
        return msg


    @staticmethod
    def get_dpi(img):
        try:
            return round(img.info["dpi"][0])
        except:
            return None
    
    
    def remover_fundo(self,image:str,output_file:str):
        image_sem_fundo = remove(image)
        image_sem_fundo.save(output_file)
    
    
    
    # def save():
    
    
    


if __name__ == "__main__":
    photopy = PhotoPy()
    image = photopy.open_image(
        "images_teste/wide-angle-shot-two-women-walking-beach-with-surfing-boards.jpg", isgray=False)
    # image.show()
    image_sem_fundo = rembg.remove(image)

    image_sem_fundo.save("sem_fundo.png")
