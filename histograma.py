# Importing modules
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
from skimage.color import rgb2hsv
from skimage.util import img_as_ubyte #img_as_ubyte Convert to 8-bit uint.
from numpy import asarray

c = io.imread('original_images/chickens.png')
io.imshow(c)


