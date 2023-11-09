import cv2
import pandas
import csv
import time

from datetime import datetime


status_list = [None, None]
times = []

# Dataframe to store time in which object appears and moves out of frame
data_frame = pandas.DataFrame(columns=['start', 'end'])

# Create a videocapture object using webcam
cam = cv2.VideoCapture(0)

first_frame = None


while True:
    check, frame = cam.read()

    # At beginning of frame object is not present
    status = 0

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

        # Changing status value when object is detected
        status = 1

        # Getting cocordinates to draw a rectangle
        (x, y, w, h) = cv2.boundingRect(contour)
        # Drawing rectnagle
        color = (0,255,0)   # BGR - Green color
        stroke = 2
        cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke)

    # Appending status to status_list for every frame
    status_list.append(status)

    # Checking object entry and exit with its time is loaded in to list
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())


    # Dislaying all frame types
    cv2.imshow('MOTION DETECTION', frame)
    cv2.imshow('GRAY IMAGE', gray)
    cv2.imshow('GUASSIAN BLUR', gauss_blur)
    cv2.imshow('SHOWING SUBSTRACTED FRAME', delta_frame)
    cv2.imshow('FRAME AFTER APPLYING THRESHOLD', threshold_delta)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


# Adding timestamp values to dataset
for i in range(0, len(times), 2):
    data_frame.append({'Start': times[i], 'End': times[i + 1]}, ignore_index=True)

# Writing data to csv file
data_frame.to_csv('time_check.csv')


cam.release()
cv2.destroyAllWindows()

