# Importing modules
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte #img_as_ubyte Convert to 8-bit uint.
from numpy import asarray

em = io.imread('original_images/emu.png')
print(em.shape)
print(em[150,150,:])

print(em[:,:,0])
print(em[:,:,1])
print(em[:,:,2])

emXur = io.imread('didico.jpg')
emRed = emXur[:,:,0]
io.imshow(emRed)
plt.show()
emGreen = emXur[:,:,1]
io.imshow(emGreen)
plt.show()
emBlue = emXur[:,:,2]
io.imshow(emBlue)
plt.show()

