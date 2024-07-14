# Virtual Mouse Using Hand Gestures

This project implements a virtual mouse system that uses hand gestures detected by a webcam. The system allows for mouse control and clicks through specific hand gestures, providing a touch-free way to interact with your computer. It leverages the `opencv-python`, `mediapipe`, `pyautogui`, and `time` libraries for hand detection and interaction.

## Features

- **Hand Gesture Detection:** Uses a webcam to detect hand gestures in real-time.
- **Left Click:** Performed by bringing the thumb and index fingers together.
- **Right Click:** Performed by bringing the thumb and middle fingers together.
- **Mouse Movement:** Controlled by moving the hand.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- PyAutoGUI (`pyautogui`)
- Time (standard library)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/SARFAS-P/Virtual_Mouse.git
    ```

3. Install the required dependencies:
    ```bash
    pip install opencv-python mediapipe pyautogui
    ```
3. open in VSCODE
   

## Usage

Run the script to start the virtual mouse system:

How It Works
-----------
- The webcam captures video footage of the user's hand.
- The system uses MediaPipe to detect hand landmarks.
- Depending on the detected hand gesture:
     - Mouse movement is controlled by the hand's position.
     - Left click is performed by bringing the thumb and index fingers together.
     - Right click is performed by bringing the thumb and middle fingers together.
- PyAutoGUI is used to simulate mouse movements and clicks based on the detected gestures.
  
Contributing
-----------
- Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

