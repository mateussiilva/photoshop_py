from PIL import Image
import os
import glob


HOME = "/home/mateus/"

PATH_SOURCE = os.path.join(HOME,"Imagens")

def get_images(path,extensions=(".png",".jpeg",".jpg")) -> list:
    for file in os.listdir(path):
        p_comepleto = os.path.join(PATH_SOURCE,file)
        if os.path.isfile(p_comepleto):
            
            print(file)




if __name__ == "__main__":
    get_images(PATH_SOURCE)
