# Importing modules
import skimage.io as io

# Reading image using imread
image=io.imread('./original_images/wombats.png')

#Print image dimensions
dimensions=image.shape
print('image dimensions',dimensions)

# select image output
image=image[0:150,0:150]

# Displaying read image
io.imshow(image)
io.show()