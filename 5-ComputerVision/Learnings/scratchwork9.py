#to detect face
# we use Cascades , need to learn how to create cascade
import cv2
faceCascade= cv2.CascadeClassifier("/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/haarcascade_frontalface_default.xml")



img= cv2.imread("/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/frnds.jpeg")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces= faceCascade.detectMultiScale(grayImg,1.9,4)
for(x,y,h,w) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("img",img)
cv2.waitKey(0)