import numpy as np
import cv2
import dlib
from math import hypot
import socket
import datetime

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#serversocket.connect(('192.168.0.6', 3232))
serversocket.connect(('192.168.1.195', 3232))

cap = cv2.VideoCapture(0)
blink_flag = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("supportingFiles/shape_predictor_68_face_landmarks.dat")

def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))
    hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)
    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
    ratio = hor_line_lenght / ver_line_lenght
    return ratio

time_stop = datetime.datetime.now().second + 15

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:

        landmarks = predictor(gray, face)
        landmarks = predictor(gray, face)
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
        if blinking_ratio > 5.7:
            serversocket.send(b'zap')
            cv2.putText(frame, "BLINKING", (50, 150), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255))
            blink_flag = 1

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if blink_flag or datetime.datetime.now().second == time_stop:
        break

cap.release()
cv2.destroyAllWindows()