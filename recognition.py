import imutils
import numpy as np
import pickle
import cv2
import face_recognition
import report
from datetime import datetime
import pytz

def record(id, attendance,late_time):
    studentNumber = report.getStudentNumber()
    nameIndex = studentNumber[studentNumber['Student Number'] == id].index.values[0]
    current_time = datetime.strftime(datetime.now(pytz.timezone('Asia/Manila')), "%H:%M:%S")
    if (attendance[nameIndex] == 'Absent')and(attendance[nameIndex] != 'Present'):
        if(current_time>late_time):
            attendance[nameIndex] = 'Late'
        else:
            attendance[nameIndex] = 'Present'
    return attendance


def main(late_time, absent_time):
    studentNumber = report.getStudentNumber()
    attendance = ['Absent'] * len(studentNumber)
    cap = cv2.VideoCapture(0)
    encoding = 'pickle\module.pkl'
    data = pickle.loads(open(encoding, "rb").read())
    if cap.isOpened:
        ret, frame = cap.read()
    else:
        ret = False
    while (ret):
        current_time = datetime.strftime(datetime.now(pytz.timezone('Asia/Manila')), "%H:%M:%S")
        print(current_time)
        print(absent_time)
        if (current_time > absent_time):
            cv2.destroyAllWindows()
            cap.release()
            print(attendance)
            report.update(attendance)
            return

        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = imutils.resize(frame, width=400)
        r = frame.shape[1] / float(rgb.shape[1])

        boxes = face_recognition.face_locations(rgb, model="hog")
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []

        for encoding in encodings:
            matches = face_recognition.compare_faces(np.array(encoding), np.array(data["encodings"]), tolerance=0.4)
            name = "Unknown"
            result = face_recognition.face_distance(np.array(encoding),np.array(data["encodings"]))
            print(np.amin(result))
            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                    name = max(counts, key=counts.get)
                    attendance=record(name,attendance,late_time)

            names.append(name)

        for ((top, right, bottom, left), name) in zip(boxes, names):
            top = int(top * r)
            right = int(right * r)
            bottom = int(bottom * r)
            left = int(left * r)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        cv2.imshow("Check Attendance", frame)
        if cv2.waitKey(1) == 27:
            break



