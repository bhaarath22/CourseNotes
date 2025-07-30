import cv2
# # #img =cv2.imread()
# # #img=cv2.imread(r'ComputerVision/Resource/WhatsApp Image 2024-09-09 at 19.24.49 (1).jpeg')
# # img=cv2.imread('/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/WhatsApp Image 2024-09-09 at 19.24.49 (1).jpeg')
# # if img is not None:
# #  cv2.imshow('ganesh',img)
# #  cv2.waitKey(0)

#READ A IMAGE AND SHOW

# try:
#     img = cv2.imread('/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/ganesh.jpeg')
#     if img is None:
#         print("Error: Unable to read image")
#     else:
#         # Process the image
#       #  cv2.imshow('Image', img)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
# except Exception as e:
#     print(f"Error: {e}")

#READ A VIDEO AND SHOW

# Srobot=cv2.VideoCapture("/Users/bharathgoud/PycharmProjects/machineLearing/ComputerVision/Resource/SpiderRobot.mp4")
# while True:
#     success,video=Srobot.read()
#     cv2.imshow("spiderRobot", video)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#       break

# WEBCAM INTEGRATION OR USING
cap=cv2.VideoCapture(0)
cap.set(3,640)#width
cap.set(4,480)#height
cap.set(10,100)#brightness
while True:
    success,video=cap.read()
    cv2.imshow("spiderRobot", video)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
      break


