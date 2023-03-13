# Importing modules
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import *
from skimage.util import img_as_ubyte 



# Reading image using imread
image_RGB_color=io.imread('wallyFinal.png')
image_gray=rgb2gray(image_RGB_color)

linha,coluna=image_gray.shape

print('Linhas:',linha,'Colunas:',coluna)


plt.imshow(image_RGB_color)
plt.show()


image_RGB_GRAY=image_RGB_color.copy()





image_RGB_GRAY[:,:,0]=img_as_ubyte(image_gray)
image_RGB_GRAY[:,:,1]=img_as_ubyte(image_gray)
image_RGB_GRAY[:,:,2]=img_as_ubyte(image_gray)

image_lab = rgb2lab(image_RGB_color)


#fig, axes = plt.subplots(2,3)


# axes[0][0].imshow(image_RGB_color)
# axes[0][0].set_title("Imagem Original")

# axes[0][1].imshow(image_gray, cmap=plt.cm.gray)
# axes[0][1].set_title("Imagem Tons de Cinza ")


# axes[0][2].imshow(image_RGB_GRAY, cmap=plt.cm.gray)
# axes[0][2].set_title("Imagem RGB Tons de Cinza")


# axes[1][0].imshow(image_RGB_GRAY[:,:,0], cmap=plt.cm.gray)
# axes[1][0].set_title("Canal R")

# axes[1][1].imshow(image_RGB_GRAY[:,:,1], cmap=plt.cm.gray)
# axes[1][1].set_title("Canal G")


# axes[1][2].imshow(image_RGB_GRAY[:,:,2], cmap=plt.cm.gray)
# axes[1][2].set_title("Canal B")


# fig.tight_layout()
# plt.show()


for i in range(linha):
	for j in range(coluna):
		if image_lab[i,j,0] > 90: 
			if image_lab[i,j,1] > -30 and image_lab[i,j,1] < 40 : 
				if image_lab[i,j,2] > 60:   
				    image_RGB_GRAY[i,j,:]=image_RGB_color[i,j,:].copy()

plt.imshow(image_RGB_GRAY)
plt.show()


fig, axes = plt.subplots(1,2)

axes[0].imshow(image_RGB_color)
axes[0].set_title("Imagem Original")


axes[1].imshow(image_RGB_GRAY)
axes[1].set_title("Imagem somente canal verde")

fig.tight_layout()
plt.show()

