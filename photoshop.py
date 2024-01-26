from PIL import Image
import cv2
import numpy as np


filename = "background_police.jpg"

img = Image.open(filename)
imgcv2 = cv2.imread(filename)
w, h, c = imgcv2.shape
print(c)
print(h)
# img.show()
