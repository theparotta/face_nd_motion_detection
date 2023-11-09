import cv2

# Create a videocapture object using webcam
cam = cv2.VideoCapture(0)

first_frame = None

while True:
    check, frame = cam.read()

    # Conversion to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Conversion to guassian blur
    gauss_blur = cv2.GaussianBlur(gray, (21,21), 0)

    # Check if inital frame is saved or not
    if first_frame is None:
        first_frame = gauss_blur
        continue

    # Calculate difference bw first_frame and subsquent frames
    delta_frame = cv2.absdiff(first_frame, gauss_blur)

    # Providing a threshold so that pixel value greated than threshold is 
    # converted to white and lower value is converted to black
    THRESHOLD = 30
    threshold_delta = cv2.threshold(delta_frame, THRESHOLD, 255, cv2.THRESH_BINARY)[1]
    threshold_delta = cv2.dilate(threshold_delta, None, iterations=0)

    # Defning contour area, ie.adding borders
    (cnts,_) = cv2.findContours(threshold_delta.copy(), cv2.RETR_EXTERNAL,
                                                       cv2.CHAIN_APPROX_SIMPLE)

    # Removing Noises and shadows by rejecting pixel values lower than a set threshold
    CONTOUR_THRESHOLD = 1000
    for contour in cnts:
        if cv2.contourArea(contour) < CONTOUR_THRESHOLD:
            continue

        # Getting cocordinates to draw a rectangle
        (x, y, w, h) = cv2.boundingRect(contour)
        # Drawing rectnagle
        color = (0,255,0)   # BGR - Green color
        stroke = 2
        cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke)


    # Dislaying all frame types
    cv2.imshow('MOTION DETECTION', frame)
    cv2.imshow('GRAY IMAGE', gray)
    cv2.imshow('GUASSIAN BLUR', gauss_blur)
    cv2.imshow('SHOWING SUBSTRACTED FRAME', delta_frame)
    cv2.imshow('FRAME AFTER APPLYING THRESHOLD', threshold_delta)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

