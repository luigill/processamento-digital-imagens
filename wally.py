# Importing modules
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
from skimage.color import rgb2hsv
from skimage.util import img_as_ubyte #img_as_ubyte Convert to 8-bit uint.
from numpy import asarray

#em = io.imread('wallyFinal.png')
#emRed = em[:,:,0]
#io.imshow(emRed)
#plt.show()
#emGreen = em[:,:,1]
#io.imshow(emGreen)
#plt.show()
#emBlue = em[:,:,2]
#io.imshow(emBlue)
#plt.show()

imgRgbColor = io.imread('wallyFinal.png')
imgGray = rgb2gray(imgRgbColor)
imgRgbGray = imgRgbColor.copy()
#imgRgbGray[:,:,0] = img_as_ubyte(imgGray)
#imgRgbGray[:,:,1] = img_as_ubyte(imgGray)
#imgRgbGray[:,:,2] = img_as_ubyte(imgGray)
#io.imshow(imgRgbGray)
#plt.show()
#io.imshow(imgHsv[:,:,0])
#plt.show()

for i in range(imgRgbColor.shape[0]) :
    for j in range(imgRgbColor.shape[1]) :
       if ((imgRgbColor[i,j,0] > 100) and (imgRgbColor[i,j,1] > 34) and (imgRgbColor[i,j,2] > 100)) :
            imgRgbColor[i,j,:] = [255,0,0]

io.imshow(imgRgbColor)
plt.show()
