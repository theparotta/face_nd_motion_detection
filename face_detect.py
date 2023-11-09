import cv2

# Importing FrontFace detecting classifier
face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')

# Reading image from photo
img = cv2.imread('ntesla.jpg')

# Deriving the gray scale of the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# MAtching pattern based on classifier
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

# Drawing rectangle over the detected face
color = (0,255,0)   # BGR
stroke = 2          # Thickness of rectangle
for x,y,w,h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), color, stroke)

# Displaying image
cv2.imshow('DETECTED', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
