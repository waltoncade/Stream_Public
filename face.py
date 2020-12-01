import numpy as np
import cv2
import dlib
from math import hypot
import socket
import datetime

from threading import Thread

class FaceDetection(Thread):
    
    def __init__(self, num_face:int, ratio:float, left_right:bool=False) -> None:
        Thread.__init__(self)
        self.ratio_limit = ratio
        self.num_face = num_face
        self.left_right = left_right
        
    def relative_face_pos(self, faces:list) -> list:
        self.sort_faces()
        return [face.left() for face in faces]
    def sort_faces(self)-> list:
        return self.faces.sort(key=lambda  x: x.left())

    @staticmethod
    def midpoint(point1=int, point2=int) -> int:
        return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)
    @staticmethod
    def face_contour(points:list, facial_landmarks:list) -> int:
        length = 0
        for i in range(0,len(points)-1):
            point_1 = (facial_landmarks.part(points[i]).x, facial_landmarks.part(points[i]).y)
            point_2 = (facial_landmarks.part(points[i+1]).x, facial_landmarks.part(points[i+1]).y)
            cv2.line(frame, point_1, point_2, (0, 255, 0), 1)
            length = length + hypot((point_1[0] - point_2[0]), (point_1[1] - point_2[1]))
        return length


    def run(self):
        cap = cv2.VideoCapture(0)
        blink_flag = 0

        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("supportingFiles/shape_predictor_68_face_landmarks.dat")
        while(True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            self.faces = detector(gray)
            for face in self.sort_faces():
                landmarks = predictor(gray, face)
                len1 = face_contour(list(range(0,16)), landmarks)
                mouth = list(range(48,67))
                mouth.append(60)
                len2 = face_contour(mouth, landmarks)
                ratio = len1/len2
                try:
                    if self.left_right: 
                        if ratio < self.ratio_limit and self.faces.index(face) == 0:
                            cv2.putText(frame, "Left Smiling", (50, 150), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255))
                        elif ratio < self.ratio_limit and self.faces.index(face) == 1:
                            cv2.putText(frame, "Right Smiling", (50, 250), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255))
                    else:
                        if ratio < self.ratio_limit:
                            cv2.putText(frame, 'Face #{faceid} is Smiling'.format(self.faces.index(face)), (50, 150), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255))
                except:
                    middle = frame[0]/2
                    if ratio < 1.2:
                        cv2.putText(frame, "Smiling", (50, 150), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255))

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

def main():
    f = FaceDetection(num_faces = 2, ratio = 1.2, left_right = True)
    f.start()

if __name__ == '__main__':
    main()