import cv2
img = cv2.imread("/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/ganesh.jpeg")
print(img.shape)

resizeimg=cv2.resize(img,(400,300))#widht,height
print(resizeimg.shape)

cropimg=img[0:2016,1400:2900] #height,width

cv2.imshow("img",img)
cv2.imshow("imgresize",resizeimg)
cv2.imshow("cropimg",cropimg)
cv2.waitKey(0)
