import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('one.jpg',0)
img2 = cv2.imread('PHOTO.jpg',0)
# cv2.imshow('image',img1)         # opencv reads the image in the "BGR" format

#plt.imshow(img1)
#plt.xticks([]),plt.yticks([])
#plt.show()          # matplotlib reads the image in the "RBG" format

titles = ['image 1','image 2']
images = [img1,img2]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()

#cv2.waitKey(0)   # here, the defined argument has unit "ms".
#cv2.destroyAllWindows()
