import os
# --- THE MAGIC FIX ---
# This forces the library to use a compatible mode, preventing the "Symbol not found" crash
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# Setup MediaPipe
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Eye Indices (Standard)
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

def calculate_ear(landmarks, indices):
    # Vertical lines
    p2_p6 = np.linalg.norm(np.array(landmarks[1]) - np.array(landmarks[5]))
    p3_p5 = np.linalg.norm(np.array(landmarks[2]) - np.array(landmarks[4]))
    # Horizontal line
    p1_p4 = np.linalg.norm(np.array(landmarks[0]) - np.array(landmarks[3]))
    return (p2_p6 + p3_p5) / (2.0 * p1_p4)

class VideoProcessor(VideoTransformerBase):
    def __init__(self):
        self.frame_counter = 0
        self.drowsy_alert = False
        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        results = self.face_mesh.process(img_rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = img.shape
                
                # Get points
                def get_pt(idx):
                    lm = face_landmarks.landmark[idx]
                    return [int(lm.x * w), int(lm.y * h)]

                left_pts = [get_pt(i) for i in LEFT_EYE]
                right_pts = [get_pt(i) for i in RIGHT_EYE]

                # Calculate EAR
                left_ear = calculate_ear(left_pts, [])
                right_ear = calculate_ear(right_pts, [])
                avg_ear = (left_ear + right_ear) / 2.0

                # Logic
                if avg_ear < 0.25:
                    self.frame_counter += 1
                else:
                    self.frame_counter = 0
                    self.drowsy_alert = False

                if self.frame_counter > 15:
                    cv2.putText(img, "DROWSINESS ALERT!", (50, 100), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

                # Visuals
                cv2.polylines(img, [np.array(left_pts)], True, (0, 255, 0), 1)
                cv2.polylines(img, [np.array(right_pts)], True, (0, 255, 0), 1)
                cv2.putText(img, f"EAR: {avg_ear:.2f}", (30, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        return img

st.title("SafeGuard: Drowsiness Detector")
st.write("Allow camera access. Close eyes to test.")

webrtc_streamer(key="drowsiness", video_processor_factory=VideoProcessor)