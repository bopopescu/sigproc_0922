import cv2
import imutils.paths as paths
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton
from PyQt5.QtCore import Qt
import face_recognition
import pickle
import os
import sys


class training(QMainWindow):

    def __init__(self):
        super().__init__()

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.setValue(0)

        self.setWindowTitle("Retraining")
        self.setGeometry(32, 32, 250, 150)

        self.btn = QPushButton('Start', self)
        self.btn.move(70,70)
        self.btn.clicked.connect(self.train)
        self.show()

        # self.btn.clicked.connect(self.train)

    def train(self):
        self.btn.setEnabled(False)
        dataset = 'dataset\\'# path of the data set
        module = 'pickle\\module.pkl' # were u want to store the pickle file

        imagepaths = list(paths.list_images(dataset))
        knownEncodings = []
        knownNames = []
        self.pbar.setValue(0)

        for (i, imagePath) in enumerate(imagepaths):
            self.pbar.setValue((i+1)/len(imagepaths)*100)
            print("[INFO] processing image {}/{}".format(i + 1,len(imagepaths)))
            print("imagePath", imagePath)
            name = os.path.split(imagePath)[0]
            name = os.path.split(name)[1]
            print("name", name)
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb, model= "hog")
            encodings = face_recognition.face_encodings(rgb, boxes)
            for encoding in encodings:
               knownEncodings.append(encoding)
               knownNames.append(name)
               print("[INFO] serializing encodings...")
               data = {"encodings": knownEncodings, "names": knownNames}
               output = open(module, "wb")
               pickle.dump(data, output)
               output.close()
        self.close()




