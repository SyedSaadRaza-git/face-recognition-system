from deepface import DeepFace
import cv2
import os
import time

camera = cv2.VideoCapture(0)

print("Starting Face Recognition System...")
print("Press 'q' to quit")

last_recognition_time = 0
recognition_interval = 2  # seconds

recognized_name = "Scanning..."

while True:

    ret, frame = camera.read()

    if not ret:
        break

    current_time = time.time()

    # Run recognition every 2 seconds
    if current_time - last_recognition_time > recognition_interval:

        try:

            results = DeepFace.find(
    img_path=frame,
    db_path="dataset",
    enforce_detection=True,
    detector_backend="opencv",
    silent=True
)

            if len(results[0]) > 0:

                # Get best match
                best_match = results[0].iloc[0]

                distance = best_match['distance']

                print("Distance:", distance)

                # Threshold check
                if distance < 0.6:

                    person_path = best_match['identity']

                    recognized_name = os.path.basename(
                        os.path.dirname(person_path)
                    )

                else:
                    recognized_name = "Unknown Person"

            else:
                recognized_name = "Unknown Person"

        except:
            recognized_name = "No Face Detected"

        last_recognition_time = current_time

    # Display result
    cv2.putText(frame,
                recognized_name,
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()