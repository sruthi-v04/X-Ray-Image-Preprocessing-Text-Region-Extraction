import cv2
import numpy as np
import os

input_dir = r"C:\Users\sruth\Desktop\rawCR_flash"
output_dir = r"C:\Users\sruth\Desktop\xrayimagespreprocess"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

max_width = 1200
max_height = 700

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

def process_image(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_dir, filename)
            img = cv2.imread(image_path)
            if img is None:
                print(f"Error: Unable to read the image from '{image_path}'. Skipping...")
                continue

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            resized_img = resize_image(gray_img, max_width, max_height)
            norm_img = cv2.normalize(resized_img, None, 0, 255, cv2.NORM_MINMAX)
            denoised_img = cv2.fastNlMeansDenoising(norm_img, None, 10, 7, 15)

            _, thresh = cv2.threshold(denoised_img, 150, 255, cv2.THRESH_BINARY_INV)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
            processed_img = 255 - opening

            # Edge detection
            edges = cv2.Canny(resized_img, 100, 200)
            edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            result_image_colored = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2BGR)

            # Ensure both images have the same dimensions and number of channels
            if result_image_colored.shape[:2] == edges_colored.shape[:2]:
                combined_image = cv2.addWeighted(result_image_colored, 0.7, edges_colored, 0.3, 0)
                output_image_path = os.path.join(output_dir, f"processed_{filename}")
                cv2.imwrite(output_image_path, combined_image)
                print(f"Processed image saved at {output_image_path}")
            else:
                print(f"Error: Image dimensions do not match for {filename}. Skipping...")

process_image(input_dir, output_dir)





