import cv2
import numpy as np
# img = cv2.imread('/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/ganesh.jpeg')
# grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("GaneshGrayImg",grayimg)
# cv2.waitKey(0)

img = cv2.imread('/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/ganesh.jpeg')
kernel =np.ones((5,5),np.uint8)#0-255
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# To resize the image
widht,height = 600,840
resizedgray=cv2.resize(grayimg,(widht,height))

#to Blur a Image
blurimg=cv2.GaussianBlur(resizedgray,(3,3),0)

#EdgeDetection
edgedetect=cv2.Canny(resizedgray,150,250)

#increaseEdge thickness
imgdilation=cv2.dilate(edgedetect,kernel,iterations=1)
# to make edge to thiner
imgThinner=cv2.erode(imgdilation,kernel,iterations=1)
cv2.imshow("blurImg",blurimg)
cv2.imshow("GaneshGrayImg",resizedgray)
cv2.imshow("edgesOfimage",edgedetect)
cv2.imshow("thicknessimg",imgdilation)
cv2.imshow("thinerimg",imgThinner)
cv2.waitKey(0)