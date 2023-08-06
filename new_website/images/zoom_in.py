import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('PixHtLab1.png')

pos = [0.1, 0.1]
size = [0.7, 0.7]

h, w = img.shape[:2]

pos = [int(pos[0] * h), int(pos[1] * w)]
size = [int(size[0] * h), int(size[1] * w)]

cropped = img[pos[0]:pos[0] + size[0], pos[1]:pos[1] + size[1]]

plt.imsave('PixHtLab1_zoomed.png', cropped)
