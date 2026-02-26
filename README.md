# SafeGuard AI Co-Pilot

🚗 Driver Drowsiness Detection App
A real-time **Driver Drowsiness Detection Web Application** built using **Streamlit**, **MediaPipe Face Mesh**, and **streamlit-webrtc**.
The app uses your webcam to detect facial landmarks, compute the **Eye Aspect Ratio (EAR)**, and trigger a warning alert when prolonged eye closure is detected.


## 📌 Project Overview

Driver fatigue is one of the leading causes of road accidents. This project implements a real-time computer vision system that:

* Accesses live webcam video
* Detects facial landmarks using MediaPipe Face Mesh
* Calculates Eye Aspect Ratio (EAR)
* Detects prolonged eye closure
* Displays a **DROWSINESS ALERT** warning on screen

The system runs entirely in the browser using Streamlit.


## 🧠 How It Works

1. **Webcam Stream**
   `streamlit-webrtc` captures live video from the user's webcam.

2. **Face Detection & Landmark Extraction**
   MediaPipe Face Mesh detects 468 facial landmarks.

3. **Eye Landmark Selection**
   Specific landmark indices for left and right eyes are extracted.

4. **EAR Calculation**
   The Eye Aspect Ratio is computed using:

   [
   EAR = \frac{||p2 - p6|| + ||p3 - p5||}{2 ||p1 - p4||}
   ]

5. **Drowsiness Detection Logic**

   * If EAR < 0.25 → Eye considered closed
   * If eyes remain closed for more than 10 consecutive frames → Trigger alert
   * Overlay `"DROWSINESS ALERT"` on video feed


## 🗂 Project Structure

├── app.py              # Main Streamlit application
├── utils.py            # EAR calculation and helper functions
├── requirements.txt    # Project dependencies
└── README.md


## ⚙️ Installation

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/drowsiness-detection-app.git
cd drowsiness-detection-app


### 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


### 3️⃣ Install Dependencies

pip install -r requirements.txt


## ▶️ Running the Application

streamlit run app.py

Then:

* Allow webcam access in your browser
* Face the camera
* Test normal blinking (no alert should trigger)
* Close eyes for ~0.5–1 second (alert should appear)


## 🧩 Dependencies

* streamlit
* streamlit-webrtc
* mediapipe
* opencv-python-headless
* numpy
* av

(See `requirements.txt` for exact versions.)


## 🧪 Verification Plan

### Manual Testing

* ✔ Webcam feed loads correctly
* ✔ Facial landmarks appear
* ✔ Normal blinking does NOT trigger alert
* ✔ Closing eyes for multiple frames triggers alert
* ✔ Alert disappears when eyes reopen


## 🚀 Future Improvements

* Add sound alarm system
* Add head pose detection
* Deploy to cloud with HTTPS support
* Add sensitivity calibration slider
* Store session logs


## 🎯 Key Concepts Used

* Computer Vision
* Real-Time Video Processing
* Facial Landmark Detection
* Eye Aspect Ratio (EAR)
* Streamlit Web Apps
* MediaPipe


## 📚 Learning Outcomes

This project demonstrates:

* Integration of computer vision models with web apps
* Real-time frame processing
* Practical application of geometric facial metrics
* Deployment-ready Python application structure


## 👨‍💻 Author

**Atharv Parmar**
Computer Science Undergraduate
Passionate about AI, Data Analytics, and Real-Time ML Applications
