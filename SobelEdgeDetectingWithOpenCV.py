import cv2
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread('images/starwars.jpg', 0)

sobel_x = cv2.Sobel(img, -1, 1, 0, ksize = 5)
sobel_y = cv2.Sobel(img, -1, 0, 1, ksize = 5)

Image.fromarray(sobel_y).convert('L').save('images/results/starwars_2.jpg')
