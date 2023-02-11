import cv2
import mediapipe as mp
import pyautogui
from playSound import soundGraph

def track():
    pyautogui.FAILSAFE = False
    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    index_x, index_y = 0, 0

    while True:
        _, frame = cap.read()   
        frame = cv2.flip(frame, 1) 
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):

                    x = int(landmark.x*frame_width)
                    y = int(landmark.y*frame_height)

                    if id == 8:
                        drawing_utils.draw_landmarks(frame, hand)
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        index_x = screen_width/frame_width*x
                        index_y = screen_height/frame_height*y
                            
                        if (index_x and index_y):
                            pyautogui.moveTo(index_x, index_y)
                            soundGraph(screen_width, screen_height, index_x, index_y)

        cv2.imshow('Virtual Mouse', frame)
        cv2.waitKey(1)

track()