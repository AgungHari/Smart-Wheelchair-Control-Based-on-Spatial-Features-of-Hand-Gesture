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

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.host, self.port))
            print("Terkoneksi dengan kursi roda")
            self.socket = s
        except socket.error:
            print("Mode Remote gagal, tidak terhubung ke kursi roda")

    def send(self, data):
        if self.socket:
            self.socket.send(data.encode('utf-8'))

s = SocketCommunicator(host, port)

def klasifikasi(image, model_cnn):
    img = cv2.resize(image, (128, 128))
    img = np.asarray(img) / 255.0
    img = img.astype('float32')
    X = np.expand_dims(img, axis=0)
    hasil = model_cnn.predict(X, verbose=0)

    if hasil.max() > 0.5:
        return np.argmax(hasil)
    return -1

def predict_pose(no_kamera, label_kelas):
    model_cnn = load_model('weightbapak.h5')

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose
    imsize = (640, 480)
    height, width = imsize[1], imsize[0]

    cap = cv2.VideoCapture(no_kamera, cv2.CAP_DSHOW)
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

            landmarks = results.pose_landmarks.landmark
            lm = [[lmark.x * width, lmark.y * height] for lmark in landmarks 
                  if 0.01 < lmark.x < 0.99 and 0.01 < lmark.y < 0.99]
            
            if len(lm) < 4:
                cv2.imshow('Prediksi Pose', image)
                continue

            lm = np.array(lm)
            xmin, ymin = np.int32(np.min(lm, axis=0)) - 3
            xmax, ymax = np.int32(np.max(lm, axis=0)) + 3

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
            idx = klasifikasi(cropped_image, model_cnn)
            x, y = 60, 60
            image = cv2.flip(image, 1)

            if idx >= 0:
                label = label_kelas[idx]
                cv2.putText(image, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255, 255, 0), 3)

                # Tambahkan kontrol berdasarkan kelas yang terdeteksi
                if label == "TanganKanan":
                    arah = 'A'
                    cv2.putText(image, "Kursi roda belok Kanan", (x, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                elif label == "TanganKiri":
                    arah = 'E'
                    cv2.putText(image, "Kursi roda belok Kiri", (x, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                elif label == "Maju":
                    arah = 'B'
                    cv2.putText(image, "Kursi roda maju", (x, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                elif label == "Berhenti":
                    arah = 'C'
                    cv2.putText(image, "Kursi roda berhenti", (x, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                elif label == "Mundur":
                    arah = 'D'
                    cv2.putText(image, "Kursi roda mundur", (x, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
                
                s.send(arah + '\n')

            cv2.imshow('Prediksi Pose', image)
            
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()

label_kelas = ("TanganKiri", "TanganKanan", "Berhenti", "Maju", "Mundur")

predict_pose(1, label_kelas)
