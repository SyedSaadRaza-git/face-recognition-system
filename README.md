# AI-Based Facial Recognition System

## Project Description
This project is a real-time facial recognition system using Deep Learning. It detects and recognizes faces using pretrained models and compares them with a local dataset.

## Features
- Real-time face recognition using webcam
- Dataset-based identity matching
- Unknown person detection
- Distance-based confidence system
- Built using DeepFace and OpenCV

## Technologies Used
- Python
- OpenCV
- DeepFace (FaceNet / ArcFace)
- TensorFlow

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Add dataset
Create folders inside dataset/ for each person

### 3. Run system
python face_recognition_system.py


## Project Structure
- capture_faces.py → Collect dataset images
- face_recognition_system.py → Real-time recognition
- dataset/ → Stored face images
