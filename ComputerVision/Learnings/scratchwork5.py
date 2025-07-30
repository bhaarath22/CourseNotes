#WARP prespective
import cv2
import numpy as np
img=cv2.imread("/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/frnds.jpeg")
width,height=250,350
pts1= np.float32([[397,789],[200,682],[292,719],[319,748]]) #these are tha points in the image that we need, we can get these point from paint microsoft or mac
pts2= np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("image",img)
cv2.imshow("extractedimg",imgOutput)
cv2.waitKey(0)