import cv2
import matplotlib.pyplot as plt
import time

def detect_face_in_image(image_path):
    img = cv2.imread(image_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 10))
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.show()

def detect_face_live():
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Could not open live video")
        exit()
    duration=20
    start_time = time.time()
    while True:
      result, frame = video_capture.read() 
      if not result:
           print("Error: Failed to capture video frame")
           break

      gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
      for (x, y, w, h) in faces:
          cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
      cv2.imshow("Live Video face recognition",frame)
      if time.time() - start_time > duration:
            print("Live video face recognition completed. Camera off")
            break
      if cv2.waitKey(1) & 0xFF == ord("q"):
          break

    video_capture.release()
    cv2.destroyAllWindows()

choice = input("Enter 'image' or 'live video': ")

if choice == "image":
    image_path = input("Enter the path to the image file: ")
    detect_face_in_image(image_path)
elif choice == "live video":
    detect_face_live()
else:
    print("Invalid choice.")