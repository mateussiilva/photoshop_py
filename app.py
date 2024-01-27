from photoshop import PhotoPy
from os.path import join



IMAGES_DIR = "images_teste"

photopy = PhotoPy()
for n in range(300):
    f = join(IMAGES_DIR,f"teste_{n}")
    i = photopy.criar_image(f,(100,100),color=(100,25,n))