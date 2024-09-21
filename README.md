
# Smart Wheelchair Control Based on Spatial Features of Hand Gesture.

🚀Collaborating with Rasyeedah binti Mohd Othman, this project involves training a CNN model with a dataset of hand movement pose. Real time predicted pose will then used to control wheelchair movement.

## Demo

![syeeda](https://github.com/user-attachments/assets/8471363c-1c57-4119-8833-e522a40c736b)

watch here : https://youtu.be/f_hjy_4UHfs?feature=shared

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
    
## Features

- Optimized hand gestures for controlling the wheelchair.
- A lightweight and user-friendly system.

![LOGO](https://github.com/user-attachments/assets/95a6c264-e6cd-4ea9-b378-208966d44ba6)



## Authors

- [@AgungHari](https://github.com/AgungHari)
- [@Rasyeedah](https://www.linkedin.com/in/rasyeedah-mohd-othman/)
