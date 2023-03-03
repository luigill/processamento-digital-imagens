# Importing modules
# For TIFF and JPEG images, such data is known as EXIF data, and the Python exifread library may be used
# "rb" option opens the file in binary format for reading
import exifread 

# Open image file for reading (must be in binary mode)

file_info=open('galaxy.tif','rb')
#file_info=open('bergen.jpg','rb')

# Extract image metadata
try:
	tags=exifread.process_file(file_info,details=False)
except:
	print('process_file fail')

for x in tags:
	print (x.ljust(32),':',tags[x])


