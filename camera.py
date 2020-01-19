import cv2
import time
import string
import random

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def take_picture(cam_ID):
    # FOTÓ ELKÉSZÍTÉSE:
    cam = cv2.VideoCapture(cam_ID, cv2.CAP_DSHOW)
    time.sleep(0.5)
    (_, picture) = cam.read()
    cam.release()
    
    # KÉPFELDOLGOZÁS:
    pic_grayscale = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    pic_contrast= cv2.convertScaleAbs(pic_grayscale, alpha = 1.25, beta = 0)
    (_, pic_threshold) = cv2.threshold(pic_contrast, 100, 255, cv2.THRESH_OTSU)

    file_name = random_string(length=5)

    cv2.imwrite("images/{0}.png".format(file_name), pic_threshold)

    return file_name