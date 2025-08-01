import cv2

def analyze_vada_hole(image_path):
    img = cv2.imread(image_path, 0)
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    hole_size = len(contours)
    if hole_size >= 3:
        return "Massive hole: Amma saved dal."
    elif hole_size == 2:
        return "Tea Shop Standard."
    else:
        return "No hole: Thattu Kada mystery."