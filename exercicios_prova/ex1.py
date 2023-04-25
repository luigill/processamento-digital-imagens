import skimage.io as io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

img_rgb = io.imread("didico.jpg")

img_rgb_gray = rgb2gray(img_rgb)

plt.imshow(img_rgb_gray,cmap="gray")
plt.show()

linha,coluna = img_rgb_gray.shape
print('Linhas:',linha,'Colunas:',coluna)

