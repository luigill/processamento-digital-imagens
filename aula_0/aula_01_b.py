# Importing modules
import skimage.io as io
from skimage.viewer import ImageViewer as IV

# Reading image using imread
image=io.imread('./original_images/wombats.png')

# Displaying read image
viewer=IV(image)
viewer.show()