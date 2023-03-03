# Importing modules
import matplotlib.pyplot as plt

# Reading image using imread
image=plt.imread('./original_images/wombats.png')

# Displaying read image
plt.imshow(image)
#plt.imshow(image, cmap ='gray')

plt.show()