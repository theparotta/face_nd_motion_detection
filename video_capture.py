import cv2

# 0 - denotes use of build in camera
# can also able to pass video file
cam = cv2.VideoCapture(0)

frame_count = 0

while True:
    # check - bool data type checks if python can able to read cam
    # frame - numpy array representation of image frame
    check, frame = cam.read()

    # Displaying each frame captured
    cv2.imshow('CAMERA', frame)

    # Incrementing frame count
    frame_count += 1

    # This will hold the frame for one milli second
    key = cv2.waitKey(1)
    # Breaking the loop if q is pressed
    if key == ord('q'):
        break


# Will releade the camera resource
cam.release()

print("No of frames processed: ", str(frame_count))


# Killing all windows
cv2.destroyAllWindows()
