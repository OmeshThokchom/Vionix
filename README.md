# Vionix - Hand Gesture Control System

Vionix is a Python-based application that allows you to control your computer using hand gestures. It uses your webcam to track your hand movements, providing a futuristic and intuitive way to interact with your PC. This project is currently in its early stages, with the initial functionality focused on tracking the index finger.

## Features

- **Real-time Hand Tracking:** Vionix uses the MediaPipe library to detect and track your hand in real-time.
- **Index Finger Tracking:** The system can accurately identify the tip of your index finger.
- **FPS Monitoring:** An FPS counter is displayed to monitor the performance of the application.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Vionix.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Vionix
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the `hand_tracking.py` script:**
   ```bash
   python hand_tracking.py
   ```
2. **A window will open displaying the feed from your webcam.**
3. **Position your hand in front of the camera, and you will see a circle tracking the tip of your index finger.**
4. **Press 'q' to quit the application.**

## Dependencies

- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://pypi.org/project/mediapipe/)

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
