# Image Resizing with Error Handling using OpenCV

## 🧠 Overview
This Python program demonstrates how to safely load and resize an image using **OpenCV**.  
It includes proper **error handling** with `try-except-else-finally` to make sure the program runs smoothly even if the image file is missing.  
The script resizes the image to a fixed size (500x400 pixels) and displays it in a window.

---

## 🚀 Features
- Reads an image using OpenCV  
- Handles missing file errors gracefully  
- Resizes the image to a new dimension  
- Displays the resized image in a window  
- Cleans up all windows automatically using a `finally` block  

---

## 🧩 Technologies Used
- **Python 3**
- **OpenCV (cv2)**

---

## ⚙️ How to Run
1. Install OpenCV if you haven’t already:
   ```bash
   pip install opencv-python
2.Place your image file (e.g., download.jpeg) in the same folder as the script.

3.Run the program:

python resize_image.py


4. the image is found, it will open a new window with the resized image.

5.Press any key to close the window
