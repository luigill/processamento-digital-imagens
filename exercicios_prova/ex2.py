import skimage.io as io
import matplotlib.pyplot as plt

img_rgb = io.imread("didico.jpg")
img_mirror = img_rgb[:,::-1,:]

plt.imshow(img_rgb)
plt.show()

plt.imshow(img_mirror)
plt.show()

linha,coluna = img_rgb.shape
print('Linhas:',linha,'Colunas:',coluna)

