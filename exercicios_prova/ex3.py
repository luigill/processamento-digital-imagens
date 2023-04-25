import cv2
 
# Two images
img1 = cv2.imread('didico.jpg')
img2 = cv2.imread('novo_bento_freitas.png')
 
# OpenCV expects to get BGR images, so we will convert from BGR to RGB
 
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
 
# Resize the Images. In order to blend them, the two images
# must be of the same shape
 
img1 =cv2.resize(img1,(620,350))
img2 =cv2.resize(img2,(620,350))
 
 
# Now, we can blend them, we need to define the weight (alpha) of the target image
# as well as the weight of the filter image
# in our case we choose 80% target and 20% filter
blended = cv2.addWeighted(src1=img1,alpha=0.8,src2=img2,beta=0.2,gamma=0)
 
# finally we can save the image. Now we need to convert it from RGB to BGR
 
cv2.imwrite('Blending.png',cv2.cvtColor(blended, cv2.COLOR_RGB2BGR))