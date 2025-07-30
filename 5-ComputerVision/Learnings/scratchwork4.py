import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

#print(img.shape)#its a grayscale image
#for color image

#img[:]= 255,0,0 #FOR BLUE COLOR
#cv2.line(img,(0,0),(200,300),(20,54,0),3)
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(20,54,0),3)
cv2.rectangle(img,(0,0),(200,400),(0,240,256),cv2.FILLED) #or we can HAVE THICKNESS width,height
cv2.circle(img,(400,60),45,(245,39,34),3) #widht,height
cv2.putText(img,"IAMBATMAN",(40,200),cv2.FONT_HERSHEY_DUPLEX,1,(230,0,4),2)

cv2.imshow("image",img)
cv2.waitKey(0)
