import cv2
import numpy as np

def check_pappadam_roundness(image_path):
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        return "Error: Unable to load image."

    # Resize for consistency
    img = cv2.resize(img, (500, 500))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to smooth edges
    blur = cv2.GaussianBlur(gray, (7, 7), 2)

    # Apply Canny edge detection
    edges = cv2.Canny(blur, 50, 150)

    # Morphological closing to fill gaps
    kernel = np.ones((5, 5), np.uint8)
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return "No Pappadam detected – Try zooming in or better lighting."

    # Use the largest contour (assumed to be papadam)
    largest_contour = max(contours, key=cv2.contourArea)

    area = cv2.contourArea(largest_contour)
    perimeter = cv2.arcLength(largest_contour, True)

    if perimeter == 0:
        return "Edge not clear – Try using a better contrast background."

    # 1. Circularity
    circularity = (4 * np.pi * area) / (perimeter ** 2)

    # 2. Enclosing circle ratio
    (x, y), radius = cv2.minEnclosingCircle(largest_contour)
    circle_area = np.pi * (radius ** 2)
    roundness_ratio = area / circle_area

    # 3. Bounding box aspect ratio
    x, y, w, h = cv2.boundingRect(largest_contour)
    aspect_ratio = float(min(w, h)) / max(w, h)  # closer to 1 = square or circle
    aspect_penalty = 1 if aspect_ratio >= 0.95 else aspect_ratio  # penalize non-circles

    # Combine all into a final roundness score
    final_score = (circularity * roundness_ratio * aspect_penalty)
    final_score = round(final_score, 3)
    score_percent = int(final_score * 100)

    # Generate comment
    if final_score > 0.9:
        comment = f"Marriage Feast Perfect – {score_percent}% Round!"
    elif final_score > 0.75:
        comment = f"Tea Shop Acceptable – {score_percent}% Round!"
    elif final_score > 0.6:
        comment = f"Local Tiffin Center Vibe – {score_percent}% Round!"
    else:
        comment = f"Thattukada Special – Only {score_percent}% Round!"

    return comment
























# import cv2
# import numpy as np

# def check_pappadam_roundness(image_path):
#     img = cv2.imread(image_path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (7, 7), 2)

#     # Threshold to extract contours
#     _, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     if not contours:
#         return "No Pappadam detected – Try zooming in."

#     # Use the largest contour (assumed to be Pappadam)
#     largest_contour = max(contours, key=cv2.contourArea)
#     area = cv2.contourArea(largest_contour)
#     perimeter = cv2.arcLength(largest_contour, True)

#     if perimeter == 0:
#         return "Edge not clear – Try better lighting."

#     circularity = (4 * np.pi * area) / (perimeter * perimeter)
#     circularity = round(circularity, 3)

#     if circularity > 0.9:
#         comment = f"Marriage Feast Perfect – {int(circularity * 100)}% Round!"
#     elif circularity > 0.75:
#         comment = f"Tea Shop Acceptable – {int(circularity * 100)}% Round!"
#     elif circularity > 0.6:
#         comment = f"Local Tiffin Center Vibe – {int(circularity * 100)}% Round!"
#     else:
#         comment = f"Thattukada Special – Only {int(circularity * 100)}% Round!"

#     return comment

















# import cv2

# def check_pappadam_roundness(image_path):
#     img = cv2.imread(image_path, 0)
#     img_blur = cv2.medianBlur(img, 5)

#     circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 100,
#                                param1=50, param2=30, minRadius=30, maxRadius=200)

#     if circles is not None:
#         return "Marriage Feast Perfect – 92% Round!"
#     else:
#         return "Thattukada Special – Probably an oval."