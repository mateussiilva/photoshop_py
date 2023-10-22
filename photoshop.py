from PIL import Image
import os
import sys



def get_images(path,extensions) -> list:
    imagens = []
    for file in os.listdir(path):
        p_comepleto = os.path.join(path,file)
        if os.path.isfile(p_comepleto):
            nome,exte = os.path.splitext(file)
            if exte in extensions:
                imagens.append(p_comepleto)
                
    return imagens if len(imagens) > 0 else None


def create_image():
    pass

def calc_new_height(width, height, new_width):
    return round(new_width * height / width)


def converter_pixel_cm(size_px,dpi):
    return tuple(map(lambda x: 2.54 * (x / dpi),size_px)) 


if __name__ == "__main__":
    Image.MAX_IMAGE_PIXELS = None
    PATH_SOURCE = sys.argv[1]
    EXTENSOES= (".png",".jpeg",".jpg")
    imagens = get_images(PATH_SOURCE,(".tif"))
    # print(imagens)
    img = Image.open(imagens[1])
    size = tuple(map(lambda x: round(x//2),converter_pixel_cm(img.size)))
    img.resize(size)
    img.save("redimensionada.jpg")
