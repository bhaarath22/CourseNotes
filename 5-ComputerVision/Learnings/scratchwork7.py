#DETECT COLORS IN AN IMAGE
import cv2
import numpy as np
#path="/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/ganesh.jpeg"
def empty(a):
    pass
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue max","TrackBars",179,179,empty)
cv2.createTrackbar("satu min","TrackBars",0,255,empty)
cv2.createTrackbar("satu max","TrackBars",255,255,empty)
cv2.createTrackbar("val min","TrackBars",0,255,empty)
cv2.createTrackbar("val max","TrackBars",255,255,empty)

while True:
    #img =cv2.imread(path)
    img = cv2.imread("/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/ganesh.jpeg")
    resizedimg = cv2.resize(img, (440, 340))
    Hsvimg=cv2.cvtColor(resizedimg,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue min","TrackBars")
    h_max=cv2.getTrackbarPos("Hue max","TrackBars")
    s_min=cv2.getTrackbarPos("satu min","TrackBars")
    s_max=cv2.getTrackbarPos("satu max","TrackBars")
    v_min=cv2.getTrackbarPos("val min","TrackBars")
    v_max=cv2.getTrackbarPos("val max","TrackBars")
    print(h_min,h_max,s_min,s_min,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    higher = np.array([h_max, s_max, v_max])
    mask= cv2.inRange(Hsvimg,lower,higher)
    imgresult=cv2.bitwise_and(resizedimg,resizedimg,mask=mask)

    # cv2.imshow("Image",resizedimg)
    # cv2.imshow("hsvImage",Hsvimg)
    # cv2.imshow("mask",mask)
    # cv2.imshow("result",imgresult)

    imgStack= stackImages(0.5,([resizedimg,Hsvimg],[mask,imgresult]))
    cv2.imshow("stackResult",imgStack)
    cv2.waitKey(1)
