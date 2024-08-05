import cv2

# Initialize the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the webcam
cap = cv2.VideoCapture(0)

# Initialize the list of trackers and other variables
trackers = []
frame_counter = 0
detect_interval = 5  # Detect faces every 5 frames
init_tracking = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    if frame_counter % detect_interval == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Create a new tracker for each detected face
        new_trackers = []
        for (x, y, w, h) in faces:
            tracker = cv2.TrackerCSRT_create()
            bbox = (x, y, w, h)
            tracker.init(frame, bbox)
            new_trackers.append(tracker)
        
        # Update the trackers list
        trackers = new_trackers
        init_tracking = True

    if init_tracking:
        # Update each tracker
        for tracker in trackers:
            success, bbox = tracker.update(frame)
            if success:
                x, y, w, h = [int(v) for v in bbox]
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Optionally, re-detect faces if tracking fails
        if len(trackers) == 0:
            init_tracking = False

    frame_counter += 1
    cv2.imshow('Multiple Face Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
