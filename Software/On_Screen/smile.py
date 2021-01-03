import numpy as np
import cv2
import dlib
from math import hypot
import socket
import datetime
import time

cap = cv2.VideoCapture(0)
blink_flag = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("supportingFiles/shape_predictor_68_face_landmarks.dat")

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#serversocket.connect(('192.168.0.6', 3232))
serversocket.connect(('192.168.1.195', 3232))

lips = [[61,62,63],[67,66,65]]
cheek_right = [[48,60],[3,4]]
cheek_left = [[54,64],[13,12]]

left_zap_time = datetime.datetime.now()
left_zap_array = []
right_zap_time = datetime.datetime.now()
right_zap_array = []
delta = datetime.timedelta(seconds=10)

def face_contour(points, facial_landmarks):
    length = 0
    for i in range(0,len(points)-1):
        point_1 = (facial_landmarks.part(points[i]).x, facial_landmarks.part(points[i]).y)
        point_2 = (facial_landmarks.part(points[i+1]).x, facial_landmarks.part(points[i+1]).y)
        cv2.line(frame, point_1, point_2, (0, 255, 0), 1)
        length = length + hypot((point_1[0] - point_2[0]), (point_1[1] - point_2[1]))
    return length/100

def left_x(faces):
    if faces[0].left() <= faces[1].left():
        return faces[0].left()
    else:
        return faces[1].left()

def point_distance(points, facial_landmarks):
    length_x = 0
    length_y = 0
    for i in range(0, len(points[0])):
        point_1 = (facial_landmarks.part(points[0][i]).x, facial_landmarks.part(points[0][i]).y)
        point_2 = (facial_landmarks.part(points[1][i]).x, facial_landmarks.part(points[1][i]).y)
        length_x = length_x + (point_1[0] - point_2[0])
        length_y = length_y + (point_1[1] - point_2[1])
    
    return abs(length_x/len(points[0])), abs(length_y/len(points[0]))

def smilecorners(points, facial_landmarks):
    point_1 = (facial_landmarks.part(points[0]).x, facial_landmarks.part(points[0]).y)
    point_2 = (facial_landmarks.part(points[1]).x, facial_landmarks.part(points[1]).y)
    point_3 = (facial_landmarks.part(points[2]).x, facial_landmarks.part(points[2]).y)
    length_x = point_2[0] - point_1[0]
    length_y = point_3[1] - point_1[1]
    length = length_x + length_y
    return length
    
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        chin = face_contour(list(range(0,16)), landmarks)
        smilen = smilecorners([48,54,57], landmarks)
        lipx, lipy = point_distance(lips, landmarks)
        cheeklx, cheekly = point_distance(cheek_left, landmarks)
        cheekrx, cheekry = point_distance(cheek_right, landmarks)
        mouth = list(range(48,67))
        mouth.append(60)
        len2 = face_contour(mouth, landmarks)
        ratio = chin/len2
        try:
            if ratio < 1.2 and left_x(faces) == face.left():
                cv2.putText(frame, "Left Smiling", (face.left() - 35, face.top() - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
                left_zap_array.append(1)
                if ((datetime.datetime.now() >= left_zap_time) and (len(left_zap_array)==10)):
                    serversocket.send(bytes("zap", "utf-8"))
                    left_zap_time = datetime.datetime.now() + delta
                    left_zap_array.clear()
            elif ratio < 1.2 and left_x(faces) <= face.left():
                cv2.putText(frame, "Right Smiling", (face.left() - 35, face.top() - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
                right_zap_array.append(1)
                if ((datetime.datetime.now() >= right_zap_time) and (len(right_zap_array)==10)):
                    serversocket.send(bytes("zap", "utf-8"))
                    right_zap_time = datetime.datetime.now() + delta
                    right_zap_array.clear()
            if(len(left_zap_array) >= 10):
                left_zap_array.clear()
            if(len(right_zap_array) >= 10):
                right_zap_array.clear()

        except:
            middle = frame[0]/2
            if ratio < 1.2:
                cv2.putText(frame, "Smiling", (face.left(), face.top() - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.05)

cap.release()
cv2.destroyAllWindows()