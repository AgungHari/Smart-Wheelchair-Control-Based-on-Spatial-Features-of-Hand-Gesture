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

The testing was conducted at Tower 2 ITS, using human gesture samples shown in the video on the left. In the video on the right, testing was performed to evaluate the success of class invocation for each gesture.

<div align="center">
  <img src="https://github.com/user-attachments/assets/8471363c-1c57-4119-8833-e522a40c736b" alt="agungyolo" width="300"/>
  <img src="https://github.com/user-attachments/assets/c2dc07a4-b8cc-411c-b2eb-a193cfacf92f" alt="agungyolo" width="300" />
</div>

[![YouTube](https://img.shields.io/badge/ComingSoon-black?style=flat-square&logo=youtube)](https://youtu.be/f_hjy_4UHfs)

Based on the test results, the following conclusions can be drawn:

![Test](https://img.shields.io/badge/Test_Success_Rate-90_above-green)
![FPS](https://img.shields.io/badge/FPS_Diff-6.386fps-red)

- The wheelchair can be controlled using the user’s hand gestures, captured by a camera mounted on the electric wheelchair. During testing, an average frame rate (FPS) of 6.3866 was recorded over 30 trials, with the highest FPS reaching 6.93 and the lowest at 5.83. This data demonstrates that the system operates consistently on the device used. 
- Further testing was conducted to evaluate the model's ability to detect and predict different gesture classes from a new user's pose. For the "TanganKanan" class, a success rate of 94\% was achieved with a 6% failure rate, while the "TanganKiri" class had a 95% success rate and a 5% failure rate. The "Berhenti" class showed a 96% success rate with a 4% failure rate. For the "Maju" class, the system achieved a 92% success rate and an 8% failure rate, while the "Mundur" class had a success rate of 93% and a failure rate of 7%.

## Installation

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
## Contributing

I am open to contributions and collaboration. If you would like to contribute, please create a pull request or contact me directly!
- Fork this repo.
- Create a new feature branch:

```bash
git checkout -b new-feature
```

- Commit your changes.
```bash
git commit -m "ver..."
```

- Push to the branch:
```bash
git push origin new-feature
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

