import numpy as np
import os
import cv2


def capturePhoto(id):
    print('creating dataset')
    face_cascade = cv2.CascadeClassifier('venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    path = 'dataset/'

    try:
        os.mkdir(path+str(id))
        print("Directory " , path+str(id),  " Created ")
    except FileExistsError:
        print("Directory " , path+str(id) ,  " already exists")
    sampleN=0;

    while 1:
        ret, img = cap.read()
        frame = img.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)
        for (x,y,w,h) in faces:
            sampleN=sampleN+1;
            print("Saving frame#" + str(sampleN))
            cv2.imwrite(path+str(id)+ "\\" +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.waitKey(100)
        cv2.imshow('Capturing Photo',img)
        cv2.waitKey(1)
        if sampleN > 99:
            break

    cap.release()
    cv2.destroyAllWindows()