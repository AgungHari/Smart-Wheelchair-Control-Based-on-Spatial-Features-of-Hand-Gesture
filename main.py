
import tensorflow as tf
import cv2
import mediapipe as mp
import numpy as np
import datetime
import time
from keras.models import load_model
import socket
import copy

# ESP32 address
host = "172.20.10.10"
port = 8080

class SocketCommunicator:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.socket = None
        self.connect()
        pass

    def connect(self):
        s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.host, self.port))
            print("Terkoneksi dengan kursi roda")
            self.socket = s
        except socket.error:
            print("Mode Remote anjay")
            


    def send(self, data):
        if self.socket:
            self.socket.send(data)

s = SocketCommunicator(host, port)


def Klasifikasi(Image, ModelCNN):
    X = []
    img = copy.deepcopy(Image)
    img = cv2.resize(img, (128, 128))
    img = np.asarray(img) / 255
    img = img.astype('float32')
    X.append(img)
    X = np.array(X)
    X = X.astype('float32')
    hs = ModelCNN.predict(X, verbose=0)

    if hs.max() > 0.5:
        idx = np.max(np.where(hs == hs.max()))
    else:
        idx = -1

    return idx

def PredictPose(NoKamera, LabelKelas):
    ModelCNN = load_model('weightbapak.h5') 

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose
    imsize = (640, 480)
    height = imsize[1]
    width = imsize[0]

    cap = cv2.VideoCapture(NoKamera, cv2.CAP_DSHOW)
    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
      
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue
    
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, imsize)
     
            results = pose.process(image)
            if not results.pose_landmarks:
                continue
            lm = []
        
            for lmark in results.pose_landmarks.landmark:
                if (lmark.x > 0.01) and (lmark.x < 1 - 0.01) and (lmark.y > 0.01) and (lmark.y < 1 - 0.01):
                    m = [lmark.x * width, lmark.y * height]
                    lm.append(m)
            if len(lm) < 4:
                cv2.imshow('Prediksi Pose', image)
                continue
            lm = np.array(lm)
            x = lm[:, 0]
            y = lm[:, 1]
            ymin = np.min(y)
            ymax = np.max(y)
            xmin = np.min(x)
            xmax = np.max(x)
            
            ymin = np.int32(np.min(y)) - 3
            ymax = np.int32(np.max(y)) - 3
            xmin = np.int32(np.min(x)) + 3
            xmax = np.int32(np.max(x)) + 3
    
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            bimage = np.zeros((height, width, 3), np.uint8)
            cv2.rectangle(bimage, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
    
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
            )
            
            mp_drawing.draw_landmarks(
                bimage,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
            )
            cropped_image = bimage[ymin:ymax, xmin:xmax, :]
            idx = Klasifikasi(cropped_image, ModelCNN)
            x = 60
            y = 60
            image = cv2.flip(image, 1)
    
            if idx >= 0:
                cv2.putText(image, LabelKelas[idx], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 0), 3)
                # Tambahkan kontrol berdasarkan kelas yang terdeteksi
                if LabelKelas[idx] == "TanganKanan":
                    print("e")  # Kontrol untuk TanganKanan
                    arah = 'A\n'
                    s.send(arah.encode('utf-8'))
                elif LabelKelas[idx] == "TanganKiri":
                    print("a")  # Kontrol untuk TanganKiri
                    arah = 'E\n'
                    s.send(arah.encode('utf-8'))
                elif LabelKelas[idx] == "Maju":
                    print("b")  # Kontrol untuk Maju
                    arah = 'B\n'
                    s.send(arah.encode('utf-8'))
                elif LabelKelas[idx] == "Berhenti":
                    arah = 'C\n'
                    s.send(arah.encode('utf-8'))
                    print("c")  # Kontrol untuk Berhenti
                elif LabelKelas[idx] == "Mundur":
                    print("d")  # Kontrol untuk Mundur
                    arah = 'D\n'
                    s.send(arah.encode('utf-8'))
                
            cv2.imshow('Prediksi Pose', image)
            
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()
    
LabelKelas=("TanganKiri",
             "TanganKanan", "Berhenti", "Maju", "Mundur")

PredictPose(1,LabelKelas)
