import cv2
import mediapipe as mp
import numpy as np

def detect_hair_color(image, bbox):
    """Extract top of head region and detect bright/colored hair."""
    h, w, _ = image.shape
    xmin = int(bbox.xmin * w)
    ymin = int(bbox.ymin * h)
    width = int(bbox.width * w)
    height = int(bbox.height * h)

    # Crop top hair region
    hair_region = image[max(0, ymin - height//2):ymin, xmin:xmin + width]
    if hair_region.size == 0:
        return False

    hsv = cv2.cvtColor(hair_region, cv2.COLOR_BGR2HSV)
    avg_hue = np.mean(hsv[:, :, 0])
    avg_sat = np.mean(hsv[:, :, 1])
    avg_val = np.mean(hsv[:, :, 2])

    # Threshold for "colored" hair (blonde/red/bright)
    if avg_sat > 60 and avg_val > 120:
        return True
    return False

def detect_head_tilt(landmarks):
    """Rough estimate of head tilt from eye position."""
    left_eye = landmarks[0]  # Right eye from viewer perspective
    right_eye = landmarks[1]

    dx = right_eye.x - left_eye.x
    dy = right_eye.y - left_eye.y

    angle = np.degrees(np.arctan2(dy, dx))
    return abs(angle) > 10  # Tilt if angle > 10°

def kanappi_score_from_image(image_path):
    mp_face = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    face_detection = mp_face.FaceDetection(model_selection=1, min_detection_confidence=0.5)

    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_image)

    if not results.detections:
        return 0, "No face detected. You might be invisible."

    detection = results.detections[0]
    bbox = detection.location_data.relative_bounding_box
    keypoints = detection.location_data.relative_keypoints

    # --- Feature-based scoring ---
    score = 0
    comment = []

    # 1. Hair Color Check
    if detect_hair_color(image, bbox):
        score += 35
        comment.append("Colored hair detected – full swag!")

    # 2. Piercings (assume bright dots on cheek/eyebrow)
    bright_pixels = cv2.inRange(rgb_image, (200, 200, 200), (255, 255, 255))
    bright_ratio = np.sum(bright_pixels) / (image.shape[0] * image.shape[1])
    if bright_ratio > 0.002:
        score += 25
        comment.append("Facial piercings – you shine bright like a diamond.")

    # 3. Head Tilt (stylish pose)
    if detect_head_tilt(keypoints):
        score += 10
        comment.append("Stylish head tilt – full attitude!")

    # 4. Fashion (simple color variance)
    center_crop = image[image.shape[0]//2:, :]
    std_dev = np.std(center_crop)
    if std_dev > 40:
        score += 15
        comment.append("Flashy outfit detected – style points added.")

    # Final funny comment
    if score >= 80:
        comment.insert(0, "🔥 Certified Kanappi – Call police!")
    elif score >= 50:
        comment.insert(0, "🌪️ Semi-Kanappi – Still dangerous.")
    else:
        comment.insert(0, "🫧 No strong Kanappi signs – Maybe a reformed one.")

    return score, "\n".join(comment)


















# import cv2
# import mediapipe as mp
# import random

# def kanappi_score_from_image(image_path):
#     mp_face = mp.solutions.face_detection
#     face_detection = mp_face.FaceDetection(model_selection=1, min_detection_confidence=0.5)

#     image = cv2.imread(image_path)
#     results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#     if results.detections:
#         score = random.randint(60, 100)
#         comment = "Proper kanappi – Moustache approved."
#     else:
#         score = random.randint(0, 40)
#         comment = "No kanappi detected. Maybe you use facewash."
#     return score, comment