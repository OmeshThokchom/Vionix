
import cv2
import time
from index_finger_reader import IndexFingerReader

# Initialize IndexFingerReader
index_reader = IndexFingerReader()


# Open webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# For FPS calculation
prev_frame_time = 0
new_frame_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Get index finger tip coordinates using the new class
    index_tip_coords = index_reader.get_index_finger_tip(frame)

    if index_tip_coords:
        cx, cy, cz = index_tip_coords
        # Draw a circle at the index finger tip position
        cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

    # Calculate and display FPS
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps_text = f"FPS: {int(fps)}"
    cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Hand Tracking', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
index_reader.close()
cap.release()
cv2.destroyAllWindows()
