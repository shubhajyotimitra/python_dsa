# live_face_detection.py
import cv2
from deepface import DeepFace

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 = default camera

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Optional: resize frame for faster detection
    frame_resized = cv2.resize(frame, (640, 480))

    # Detect faces using DeepFace (PyTorch backend)
    try:
        faces = DeepFace.detectFace(
            frame_resized,
            detector_backend='opencv',  # CPU friendly
            enforce_detection=False
        )
    except Exception as e:
        faces = None

    # Draw a rectangle around detected faces using OpenCV
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in detected_faces:
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the video
    cv2.imshow("Live Face Detection", frame_resized)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()


