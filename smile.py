import numpy as np
import cv2
import dlib
from math import hypot
import socket
import datetime

cap = cv2.VideoCapture(0)
blink_flag = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("supportingFiles/shape_predictor_68_face_landmarks.dat")

def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

def face_contour(points, facial_landmarks):
    length = 0
    for i in range(0,len(points)-1):
        point_1 = (facial_landmarks.part(points[i]).x, facial_landmarks.part(points[i]).y)
        point_2 = (facial_landmarks.part(points[i+1]).x, facial_landmarks.part(points[i+1]).y)
        cv2.line(frame, point_1, point_2, (0, 255, 0), 1)
        length = length + hypot((point_1[0] - point_2[0]), (point_1[1] - point_2[1]))
    return length

def left_x(faces):
    if faces[0].left() <= faces[1].left():
        return faces[0].left()
    else:
        return faces[1].left()

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        len1 = face_contour(list(range(0,16)), landmarks)
        mouth = list(range(48,67))
        mouth.append(60)
        len2 = face_contour(mouth, landmarks)
        ratio = len1/len2
        try:
            if ratio < 1.2 and left_x(faces) == face.left():
                cv2.putText(frame, "Left Smiling", (50, 150), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255))
            elif ratio < 1.2 and left_x(faces) <= face.left():
                cv2.putText(frame, "Right Smiling", (50, 250), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255))
        except:
            middle = frame[0]/2
            if ratio < 1.2:
                cv2.putText(frame, "Smiling", (50, 150), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255))

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()