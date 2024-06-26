import os
from threading import Thread
import cv2
import time
import glob
from emailing import send_email

# initialize the video capture object to use the webcam
video = cv2.VideoCapture(0)
# allow the camera to warm up for a second
time.sleep(1)
# to store the first frame for reference
first_frame = None
# list to keep track of object status in the frame
status_list = []
# counter for image filename
count = 1


def clean_folder():
    images = glob.glob('images/*.png')
    for image in images:
        os.remove(image)


while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    # apply to threshold to the delta_frame to get a binary image
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    # dilate the threshold frame to fill in holes
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow('my video', dil_frame)

    # find contours in the binary image
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        # get the bounding box coordinates for the contour
        x, y, w, h = cv2.boundingRect(contour)
        # draw a rectangle around the contour
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            # status = 1 means that the object is in the frame
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]

    # update the status list to keep the last two statuses
    status_list.append(status)
    status_list = status_list[-2:]

    # if an object was detected in the prev frame but not in the curr frame
    # send an email
    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email, args=(image_with_object, ))
        email_thread.daemon = True
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True

        email_thread.start()

    print(status_list)

    # display the original frame with rectangle
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()

clean_thread.start()