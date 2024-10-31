[![banner3](banner3.png)](https://www.agungg.com/)

# Smart Wheelchair Control Based on Spatial Features of Hand Gesture.

![Scikit-learn version](https://img.shields.io/badge/scikitlearn-v1.5.1-black)
![Keras version](https://img.shields.io/badge/Keras-v3.5.0-darkblue)
![matplotlib version](https://img.shields.io/badge/matplotlib-v3.9.2-darkred)
![MediaPipe version](https://img.shields.io/badge/MediaPipe-v0.10.14-pink)
![Tensorflow version](https://img.shields.io/badge/Tensorflow-v2.10.1-orange)
![OpenCV version](https://img.shields.io/badge/OpenCV-v4.9.0.80-darkgreen)
![IPyKernel version](https://img.shields.io/badge/IPyKernel-v6.29.4-yellow)
![License](https://img.shields.io/badge/License-MIT-darkgray)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

Collaborating with Rasyeedah binti Mohd Othman, this project involves training a CNN model with a dataset of hand movement pose. Real time predicted pose will then used to control wheelchair movement.

## Project Result

[![syeeda](https://github.com/user-attachments/assets/8471363c-1c57-4119-8833-e522a40c736b)](https://youtu.be/f_hjy_4UHfs)

[![YouTube](https://img.shields.io/badge/YouTube-black?style=flat-square&logo=youtube)](https://youtu.be/f_hjy_4UHfs)

## Installation

PyPi version

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
    
## Features

- Optimized hand gestures for controlling the wheelchair.
- A lightweight and user-friendly system.

<p align="center">
  <img src="https://github.com/user-attachments/assets/95a6c264-e6cd-4ea9-b378-208966d44ba6" alt="LOGO" width="300">
</p>


## Authors

<img alt="Static Badge" src="https://img.shields.io/badge/AgungHari-black?style=social&logo=github&link=https%3A%2F%2Fgithub.com%2FAgungHari">
<img alt="Static Badge" src="https://img.shields.io/badge/Rasyeeda-black?style=social&logo=linkedin&link=https%3A%2F%2Fmy.linkedin.com%2Fin%2Frasyeedah-mohd-othman">

