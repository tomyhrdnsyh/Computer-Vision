import cv2
import pickle
import os

PATH = os.path.dirname(__file__)
FILE_NAME = 'car_park_pos'


class ParkingSpacePicker:
    def __init__(self):
        self.width = 107
        self.height = 48
        self.posList = None
        self.load_park_pos()

    def load_park_pos(self):
        try:
            with open(os.path.join(PATH, "data", FILE_NAME), 'rb') as file_obj:
                self.posList = pickle.load(file_obj)
        except FileNotFoundError:
            self.posList = []
            print('load failed')
        else:
            print('load success')

    def mouse_click(self, events, x, y, flags, params):
        if events == cv2.EVENT_LBUTTONDOWN:
            self.posList.append((x, y))
        if events == cv2.EVENT_RBUTTONDOWN:
            for i, coordinate in enumerate(self.posList):
                x1, y1 = coordinate
                if x1 < x < x1 + self.width and y1 < y < y1 + self.height:
                    self.posList.pop(i)
        with open('data/car_park_pos', 'wb') as file_obj:
            pickle.dump(self.posList, file_obj)

    def create_rectangle(self):
        while True:
            img = cv2.imread('data/carParkImg.png')

            for pos in self.posList:
                cv2.rectangle(img, pos, (pos[0] + self.width, pos[1] + self.height), (255, 0, 255), 2)

            cv2.imshow('Image', img)
            cv2.setMouseCallback('Image', self.mouse_click)
            cv2.waitKey(1)
