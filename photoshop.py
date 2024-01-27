from PIL import Image
from os.path import join
import rembg


Image.MAX_IMAGE_PIXELS = None


class PhotoPy:
    def __init__(self) -> None:
        self.mode = "RGB"

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

    def escreverimage(self, img, posicao,texto,colortext):
        pass

if __name__ == "__main__":
    photopy = PhotoPy()
    image = photopy.open_image(
        "images_teste/wide-angle-shot-two-women-walking-beach-with-surfing-boards.jpg", isgray=False)
    # image.show()
    image_sem_fundo = rembg.remove(image)

    image_sem_fundo.save("sem_fundo.png")
