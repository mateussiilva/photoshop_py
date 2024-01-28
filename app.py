from PIL import Image, ImageDraw, ImageFont
from photoshop import PhotoPy
import os
from os.path import join



IMAGES_DIR = "images_teste"
IMAGES  =  [join(IMAGES_DIR,i) for i in os.listdir(IMAGES_DIR) ]
photopy = PhotoPy()

def criar_images_em_branco():
    for n in range(10):
        f = join(IMAGES_DIR,f"teste_{n}")
        i = photopy.criar_image(f,(100,100),color=(255,255,255))
        
def pegar_nome_arquivo(pathfile):
    p, file = os.path.split(pathfile)
    nome, exte = os.path.splitext(file)
    return nome
        
# criar_images_em_branco()


fnt = ImageFont.truetype("fonts/BebasNeue-Regular.ttf",size=12)
for image in IMAGES:
    img = photopy.open_image(image)
    sizes = photopy.size_image(img)
    print(image)
    photopy.dados_imagem(img)
    print("---------------------------------")
    # posicao = 2,  int(sizes[1]) - 12 
    # nome = pegar_nome_arquivo(image)
    # draw = ImageDraw.Draw(img)
    # draw.text(posicao,"black",fnt)
    # img.save(image)

# out.show()