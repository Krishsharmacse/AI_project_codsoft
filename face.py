import cv2
import numpy as np
#Thankyou Codsoft for giving me this opportunity

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the new images for person_1 and person_2
person_1 = cv2.imread(r"C:\Users\SHUBHAM SHARMA\Desktop\programming\python\project.py\gandi sakal\WhatsApp Image 2025-02-09 at 2.32.33 PM.jpeg")
person_2 = cv2.imread(r"C:\Users\SHUBHAM SHARMA\Desktop\programming\python\project.py\gandi sakal\WhatsApp Image 2025-02-09 at 2.32.32 PM.jpeg")


if person_1 is None or person_2 is None:
    print("Error: One or more images failed to load.")
else:

    gray_person_1 = cv2.cvtColor(person_1, cv2.COLOR_BGR2GRAY)
    gray_person_2 = cv2.cvtColor(person_2, cv2.COLOR_BGR2GRAY)


    faces = [gray_person_1, gray_person_2]
    labels = [0, 1]


    recognizer.train(faces, np.array(labels))

    # Initialize video capture
    video_capture = cv2.VideoCapture(0)

    # List of names corresponding to the labels
    names = ["Krish Sharma", "Katapa"]

    while True:
        # Capture video frame by frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces_detected = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces_detected:
           
            roi_gray = gray[y:y+h, x:x+w]

            label, confidence = recognizer.predict(roi_gray)

      
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


            cv2.putText(frame, f'{names[label]} ({round(confidence, 2)})', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)  
            

       
        cv2.imshow('Video', frame)

       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
    video_capture.release()
    cv2.destroyAllWindows()
