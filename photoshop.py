from PIL import Image,ImageFilter
import cv2
import numpy as np
import os


IMAGE_DIR = "images_teste"
imagens = [os.path.join(IMAGE_DIR,image) for image in os.listdir(IMAGE_DIR)]

filename = imagens[0]

img = Image.open(filename)
imgcv2 = cv2.imread(filename)
w, h, c = imgcv2.shape

imgenhacent = img.filter(ImageFilter.GaussianBlur(45))
imgenhacent.show() 