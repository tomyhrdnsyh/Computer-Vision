import cv2
import cvzone
import numpy as np

from createRectangle.parkingSpacePicker import ParkingSpacePicker

# Load CarParkPos Obj
psp = ParkingSpacePicker()
posList = psp.posList
width = psp.width
height = psp.height

# Video Feed
cap = cv2.VideoCapture('createRectangle/data/carPark.mp4')


# check parking
def crop_images(img_pro):
    space_counter = 0
    for coordinate in posList:
        x, y = coordinate
        imgcrop = img_pro[y:y+height, x:x+width]
        # cv2.imshow(str(x*y), imgcrop)
        count = cv2.countNonZero(imgcrop)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=(0, 0, 255))

        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            space_counter += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv2.rectangle(img, coordinate, (coordinate[0] + width, coordinate[1] + height), color, thickness)
    cvzone.putTextRect(img, f'Free : {space_counter}/{len(posList)}', (100, 50),
                       scale=2, thickness=3, offset=20, colorR=(0, 200, 0))


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.int8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    crop_images(imgDilate)

    cv2.imshow('Image', img)
    # cv2.imshow('Image Median', imgMedian)
    # cv2.imshow('Image Dilate', imgDilate)
    cv2.waitKey(1)
