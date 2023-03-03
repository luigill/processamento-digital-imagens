# Importing modules
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte #img_as_ubyte Convert to 8-bit uint.

from numpy import asarray

# Reading image using imread
image_01=io.imread('toycars1.png')
image_02=io.imread('toycars2.png')
image_03=io.imread('toycars3.png')


image_01_grayscale=rgb2gray(image_01)
image_02_grayscale=rgb2gray(image_02)
image_03_grayscale=rgb2gray(image_03)

# Y = 0.2125 R + 0.7154 G + 0.0721 B

#plt.imshow(image_01)
#plt.show()
#plt.imshow(image_02)
#plt.show()
#plt.imshow(image_03)
#plt.show()

#plt.imshow(image_01_grayscale, cmap=plt.cm.gray)
#plt.show()
#plt.imshow(image_02_grayscale, cmap=plt.cm.gray)
#plt.show()
#plt.imshow(image_03_grayscale, cmap=plt.cm.gray)
#plt.show()

fig, axes = plt.subplots(2, 3)
#ax = axes.ravel()

axes[0][0].imshow(image_01)
axes[0][0].set_title("image_01")

axes[0][1].imshow(image_02)
axes[0][1].set_title("image_02")

axes[0][2].imshow(image_03)
axes[0][2].set_title("image_03")

axes[1][0].imshow(image_01_grayscale, cmap=plt.cm.gray)
axes[1][0].set_title("image_01_grayscale")

axes[1][1].imshow(image_02_grayscale, cmap=plt.cm.gray)
axes[1][1].set_title("image_02_grayscale")

axes[1][2].imshow(image_03_grayscale, cmap=plt.cm.gray)
axes[1][2].set_title("image_03_grayscale")

fig.tight_layout()
plt.show()

image_01_grayscale=(image_01_grayscale/3)
image_02_grayscale=(image_02_grayscale/3)
image_03_grayscale=(image_03_grayscale/3)


blend = img_as_ubyte(image_01_grayscale - image_02_grayscale - image_03_grayscale)
plt.imshow(blend, cmap=plt.cm.gray)
plt.show()

