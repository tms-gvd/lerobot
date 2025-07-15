import cv2

# import cv2

# def list_available_cameras(max_cameras=10):
#     available_cameras = []
#     for index in range(max_cameras):
#         cap = cv2.VideoCapture(index)
#         if cap.isOpened():
#             available_cameras.append(index)
#             cap.release()
#     return available_cameras

# if __name__ == "__main__":
#     cameras = list_available_cameras()
#     if cameras:
#         print("Available cameras:")
#         for cam in cameras:
#             print(f"Camera index: {cam}")
#     else:
#         print("No cameras found.")

# exit()

def display_camera_feed():
    # Initialize the camera (0 is usually the default webcam)
    cap = cv2.VideoCapture(2)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # If frame is read correctly ret is True
            if not ret:
                print("Error: Can't receive frame")
                break

            # Display the frame
            cv2.imshow('Camera Feed', frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Release the camera and destroy all windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    display_camera_feed()