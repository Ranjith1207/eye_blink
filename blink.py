import cv2
import mediapipe as mp
import numpy as np
import time
import os

def eye_aspect_ratio(eye):
  
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
  
    C = np.linalg.norm(eye[0] - eye[3])
  
    ear = (A + B) / (2.0 * C)
    return ear

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

EAR_THRESHOLD = 0.21  
CONSEC_FRAMES = 2    

blink_count = 0
blinks_detected = []
frame_counter = 0
image_captured = False

cap = cv2.VideoCapture(0)  

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        mesh = results.multi_face_landmarks[0]
        h, w, _ = frame.shape
        
        left_eye_indices = [33, 160, 158, 133, 153, 144]
        right_eye_indices = [362, 385, 387, 263, 373, 380]

        left_eye = np.array([(int(mesh.landmark[i].x * w), int(mesh.landmark[i].y * h)) for i in left_eye_indices])
        right_eye = np.array([(int(mesh.landmark[i].x * w), int(mesh.landmark[i].y * h)) for i in right_eye_indices])

        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        ear = (left_ear + right_ear) / 2.0

        if ear < EAR_THRESHOLD:
            frame_counter += 1
        else:
            if frame_counter >= CONSEC_FRAMES:
                curr_time = time.time()
                blinks_detected[:] = [t for t in blinks_detected if curr_time - t < 2.0]
                blinks_detected.append(curr_time)
                if len(blinks_detected) >= 2 and not image_captured:
                    time.sleep(1)
                    print("capturing image")
                    time.sleep(1)
                    def save_unique_image(frame, base_filename='captured_image', ext='jpg'):
                        i = 0
                        while True:
                            filename = f"{base_filename}_{i}.{ext}"
                            if not os.path.exists(filename):
                                cv2.imwrite(filename, frame)
                                break
                            i += 1
                    save_unique_image(frame)

                    print('Image captured on double blink!')
                    image_captured = True
            frame_counter = 0

        cv2.polylines(frame, [left_eye], isClosed=True, color=(0,255,0), thickness=1)
        cv2.polylines(frame, [right_eye], isClosed=True, color=(0,255,0), thickness=1)

    cv2.imshow('Eye Blink Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or image_captured:
        break

cap.release()
cv2.destroyAllWindows()
