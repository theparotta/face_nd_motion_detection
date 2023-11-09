import cv2

# cv2 stores the image as a Numpy array

# Loading a coloured image
img_colour = cv2.imread('fern.jpg', 1)
# Loading image as a grayscale
img_gray = cv2.imread('fern.jpg', 0)

# GETTING SIZE OF IMAGE
size_gray = img_gray.shape
size_color = img_colour.shape

# DISPLAYING THE IMAGE
cv2.imshow('WINDOW NAME', img_colour)
cv2.waitKey(0)                               # Wait of keypress to close window
# cv2.waitKey(2000)     # Wait for certain amount of time & automatically closed the window
cv2.destroyAllWindows()

# RESIZING IMAGE
expand = cv2.resize(img_colour, (400,300))
shrink = cv2.resize(img_gray, (int(img_gray.shape[1] / 7), int(img_gray.shape[0] / 7)))
