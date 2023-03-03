# Importing modules
import skimage.io as io

# Reading image using imread
image=io.imread('./original_images/wombats.png')

# Displaying read image
io.imshow(image)
io.show()