
import numpy as np

# MediaPipe Face Mesh Landmark Indices
# Left eye indices
LEFT_EYE = [362, 385, 387, 263, 373, 380]
# Right eye indices
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

def calculate_ear(landmarks, eye_indices):
    """
    Calculate the Eye Aspect Ratio (EAR) for a given eye.

    Args:
        landmarks: List of landmarks from MediaPipe Face Mesh.
        eye_indices: List of indices for the eye (left or right).

    Returns:
        float: The calculated EAR.
    """
    # Vertical landmarks
    p2_p6 = np.linalg.norm(np.array(landmarks[eye_indices[1]]) - np.array(landmarks[eye_indices[5]]))
    p3_p5 = np.linalg.norm(np.array(landmarks[eye_indices[2]]) - np.array(landmarks[eye_indices[4]]))

    # Horizontal landmarks
    p1_p4 = np.linalg.norm(np.array(landmarks[eye_indices[0]]) - np.array(landmarks[eye_indices[3]]))

    ear = (p2_p6 + p3_p5) / (2.0 * p1_p4)
    return ear
