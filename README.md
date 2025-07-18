# 👁️ Double Blink Image Capture using OpenCV & MediaPipe

This Python project uses **OpenCV** and **MediaPipe** to detect **eye blinks** and captures an image from your webcam when a **double blink** is detected. It's useful for hands-free camera control in accessibility, surveillance, or creative computer vision applications.

---

## 📸 Features

- Detects face and eyes using **MediaPipe Face Mesh**
- Calculates **Eye Aspect Ratio (EAR)** to detect blinks
- Captures an image automatically on **double blink**
- Saves image with a **unique filename**
- Displays live webcam feed with eye landmarks

---

## 🚀 Requirements

Make sure you have the following Python libraries installed:

```bash
pip install opencv-python mediapipe numpy
```

---

## 🧠 How It Works

1. Uses MediaPipe's facial landmarks to track eyes
2. Calculates the Eye Aspect Ratio (EAR)
3. If a double blink is detected within 2 seconds:
   - Captures an image from the webcam
   - Saves it as `captured_image_<number>.jpg`

---

## 🖥️ Usage

1. Clone the repository or copy the script.
2. Run the Python file:

```bash
python double_blink_capture.py
```

3. Look at your webcam and **double blink** to trigger the capture.
4. Press **`q`** to quit the app.

---

## 🗂️ Output

Captured images will be saved in the same directory as the script:
```
captured_image_0.jpg
captured_image_1.jpg
...
```

---

## 🛠️ File Structure

```
├── double_blink_capture.py
├── README.md
├── captured_image_0.jpg (example output)
```

---

## 📌 Notes

- The detection may vary depending on lighting and camera quality.
- Works best when the user's face is centered and visible.
- You can tweak `EAR_THRESHOLD` or `CONSEC_FRAMES` for sensitivity adjustments.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [MediaPipe](https://github.com/google/mediapipe)
- [OpenCV](https://opencv.org/)
- Inspired by computer vision and accessibility solutions.
