from PIL import Image
from pylab import *

im = array(Image.open('images/fellowship.jpg').convert('L'))

gray()

im2 = 255 - im # negative image
Image.fromarray(im2).convert('L').save("images/results/fellowship_2.jpg")

im3 = (100.0 / 255) * im + 100 # Clamp to interval 100 ... 200
Image.fromarray(im3).convert('L').save("images/results/fellowship_3.jpg")

im4 = 255.0 * (im / 255.0) ** 2
Image.fromarray(im4).convert('L').save("images/results/fellowship_4.jpg")
