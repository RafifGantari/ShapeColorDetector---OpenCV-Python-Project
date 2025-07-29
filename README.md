# 🟥🟩🟦 ShapeColorDetector from Video

## 🎯 Description
**ShapeColorDetector** is a Python project using **OpenCV** to detect and classify basic geometric shapes (circle, triangle, rectangle) along with their dominant **colors** (red, green, blue) from an `.mp4` video. It processes the video frame-by-frame, draws bounding boxes around detected shapes, and labels them based on color and form.

> 🧠 This project was developed as part of a **research internship task** in the **Abinara ITS Research Team**, focused on applying computer vision in real-world scenarios.

---

## 🛠️ Features
- Processes `.mp4` videos frame-by-frame
- Detects and classifies:
  - **Shapes**: Circle, Triangle, Rectangle
  - **Colors**: Red, Green, Blue
- Draws bounding boxes with labels such as:
  - `segi empat hijau`
  - `lingkaran merah`
  - `segitiga biru`

---

## 📸 Sample Output
> Replace with your own screenshot or video frame  
![Preview](example output.png)

---

## 💡 Technologies Used
- Python 3.x
- OpenCV
- NumPy

---

## 🧪 How It Works
1. Load the `.mp4` video using `cv2.VideoCapture()`
2. Loop through each video frame
3. Convert frame to HSV color space
4. Mask red, green, and blue color ranges
5. Detect contours and approximate shapes
6. Classify and label each shape with its color
7. Display annotated frames in real-time
