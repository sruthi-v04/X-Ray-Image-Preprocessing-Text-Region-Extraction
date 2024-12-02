import cv2
import numpy as np
import os

def resize_image(image, max_width, max_height):
    (h, w) = image.shape[:2]
    aspect_ratio = w / h

    if w > h:
        new_width = min(max_width, w)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(max_height, h)
        new_width = int(new_height * aspect_ratio)

    return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY_INV)
    return binary

def detect_text_regions(binary_image):
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    regions = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 50 and h > 20:
            regions.append((x, y, w, h))
    return regions

def extract_and_correct_text_regions(image, regions):
    extracted_text_images = []
    for (x, y, w, h) in regions:
        roi = image[y:y+h, x:x+w]
        if h > w:
            roi = cv2.rotate(roi, cv2.ROTATE_90_CLOCKWISE)
        roi_processed = preprocess_image(roi)
        extracted_text_images.append(roi_processed)
    return extracted_text_images

image_path = r"C:\Users\sruth\Desktop\xrayimagespreprocess\05-07-2022_1-XRayTest.png"
output_image_path = r"C:\Users\sruth\Desktop\bounded_after_prep\helped.png"

image = cv2.imread(image_path)

if image is None:
    print("Failed to load image.")
else:
    max_width = 1200
    max_height = 700
    resized_image = resize_image(image, max_width, max_height)

    binary_image = preprocess_image(resized_image)
    text_regions = detect_text_regions(binary_image)
    extracted_text_images = extract_and_correct_text_regions(resized_image, text_regions)

    for idx, roi in enumerate(extracted_text_images):
        cv2.imwrite(f'C:\\Users\\sruth\\Desktop\\output\\extracted_text_{idx}.png', roi)

    for (x, y, w, h) in text_regions:
        cv2.rectangle(resized_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    output_folder = os.path.dirname(output_image_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    saved = cv2.imwrite(output_image_path, resized_image)
    if saved:
        print(f"Image successfully saved at {output_image_path}")
    else:
        print("Failed to save the image.")

    cv2.imshow('Detected Text Regions', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()










