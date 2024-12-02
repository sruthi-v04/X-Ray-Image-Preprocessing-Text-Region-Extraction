# X-Ray Image Preprocessing and Text Region Extraction

## Overview
This repository provides a specialized pipeline focused on **edge detection** using the **Canny algorithm** and **thresholding techniques** (including Otsu's method) for preprocessing X-Ray images. These techniques enhance text region extraction and OCR accuracy by preparing images with clean edges and optimized contrasts.

This work is tied to my learning and application of edge detection and thresholding methods in preprocessing images for improved OCR results, as detailed in **Weeks 1-4** of my internship.

## Key Features
- **Canny Edge Detection**: Used to detect sharp edges in images, enhancing the clarity of text and structures.
- **Thresholding (Otsu’s method)**: Applied to separate text from background, improving contrast for OCR processing.
- **Preprocessing**: Includes resizing, denoising, and binarizing images to prepare them for text extraction.
- **Text Region Extraction**: Detects and isolates text regions, rotating them if necessary for OCR compatibility.
- **Combining Canny and Thresholding**: Uses Canny for edge detection and Otsu's thresholding to ensure optimal text visibility for OCR.

## Background (Weeks 1-4)
During my internship, I focused on improving OCR accuracy through preprocessing methods such as:
- **Edge Detection with Canny**: I explored the use of the Canny algorithm for edge detection, which highlights the boundaries of text in images, making it easier for OCR systems to extract text.
- **Thresholding Techniques**: I studied Otsu’s thresholding and applied it to preprocess images, balancing between the foreground and background to make text stand out more clearly in the images.
- **Linking to OCR Workflows**: I combined these preprocessing methods with OCR pipelines and deskewing techniques to improve the accuracy and reliability of text extraction from X-Ray images.

## Workflow
1. **Preprocessing**: Resize, normalize, and denoise images.
2. **Edge Detection**: Apply the Canny edge detection algorithm to enhance image features.
3. **Thresholding**: Use Otsu’s method to convert images into a binary format for better contrast between text and background.
4. **Text Region Extraction**: Detect and correct text regions, rotating if necessary.
5. **Output**: Save processed images with text regions highlighted and extracted text areas as separate images.


