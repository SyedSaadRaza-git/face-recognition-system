import cv2
import os

# Enter person name
person_name = input("Enter person name: ")

# Create folder path
dataset_path = f"dataset/{person_name}"

# Create folder if not exists
os.makedirs(dataset_path, exist_ok=True)

# Open webcam
camera = cv2.VideoCapture(0)

count = 0

print("Press 's' to save image")
print("Press 'q' to quit")

while True:

    ret, frame = camera.read()

    if not ret:
        print("Failed to capture image")
        break

    cv2.imshow("Face Capture", frame)

    key = cv2.waitKey(1)

    # Save image
    if key == ord('s'):

        image_path = f"{dataset_path}/{count}.jpg"

        cv2.imwrite(image_path, frame)

        print(f"Saved: {image_path}")

        count += 1

    # Quit
    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()