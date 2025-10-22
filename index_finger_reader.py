
import mediapipe as mp
import cv2

class IndexFingerReader:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,  # Only interested in one hand for index finger
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def get_index_finger_tip(self, frame):
        # Convert the BGR image to RGB.
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe Hands
        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            # Assuming we only care about the first detected hand for simplicity
            hand_landmarks = results.multi_hand_landmarks[0]
            index_finger_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
            
            # Get frame dimensions for scaling
            h, w, c = frame.shape
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            
            return (cx, cy, index_finger_tip.z)
        return None

    def close(self):
        self.hands.close()
