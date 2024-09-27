
# Smart Wheelchair Control Based on Spatial Features of Hand Gesture.

🚀Collaborating with Rasyeedah binti Mohd Othman, this project involves training a CNN model with a dataset of hand movement pose. Real time predicted pose will then used to control wheelchair movement.

## 🎬 Demo

![syeeda](https://github.com/user-attachments/assets/8471363c-1c57-4119-8833-e522a40c736b)

watch here : https://youtu.be/f_hjy_4UHfs?feature=shared

## 🔨 Installation

PyPi version

![Scikit-learn version](https://img.shields.io/badge/scikitlearn-v1.5.1-black)
![Keras version](https://img.shields.io/badge/Keras-v3.5.0-purple)
![matplotlib version](https://img.shields.io/badge/matplotlib-v3.9.2-red)
![MediaPipe version](https://img.shields.io/badge/MediaPipe-v0.10.14-blue)
![Tensorflow version](https://img.shields.io/badge/Tensorflow-v2.10.1-orange)
![OpenCV version](https://img.shields.io/badge/OpenCV-v4.9.0.80-green)
![IPyKernel version](https://img.shields.io/badge/IPyKernel-v6.29.4-yellow)

Please use seperate folder for training and control. venv setup for training

```bash
  python --version
  python -m venv nama_venv
  nama_venv\Scripts\activate
  pip install opencv-python
  pip install mediapipe
  pip install numpy
  pip install matplotlib
  pip install tensorflow
```
The training file include process of collecting dataset. Please modify for each class image data folder. Example :
```bash
  CreateDataSet(0, "Berhenti", DirektoriDataSet)
```
Actually, you need an ESP32 and the wheelchair to run it.

```bash
  python --version
  python -m venv nama_venv
  nama_venv\Scripts\activate
  pip install mediapipe
  pip install opencv-python
```
    
## 🍿 Features

- Optimized hand gestures for controlling the wheelchair.
- A lightweight and user-friendly system.

![LOGO](https://github.com/user-attachments/assets/95a6c264-e6cd-4ea9-b378-208966d44ba6)



## Authors

<img alt="Static Badge" src="https://img.shields.io/badge/AgungHari-black?style=social&logo=github&link=https%3A%2F%2Fgithub.com%2FAgungHari">
<img alt="Static Badge" src="https://img.shields.io/badge/Rasyeeda-black?style=social&logo=linkedin&link=https%3A%2F%2Fmy.linkedin.com%2Fin%2Frasyeedah-mohd-othman">

