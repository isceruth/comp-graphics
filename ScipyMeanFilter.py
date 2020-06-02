from PIL import Image
import scipy.ndimage
import numpy as np

a = Image.open('images/towers_noise.jpg').convert('L')

k = np.ones((5, 5)) / 25
b = scipy.ndimage.filters.convolve(a, k)
Image.fromarray(b).convert('L').save('images/results/towers_noise_2.jpg')