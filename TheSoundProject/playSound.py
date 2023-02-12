import cv2
import mediapipe as mp
import pyautogui
import pygame.midi
import numpy as np
import time
import multiprocessing
#import rtmidi

###################################################################################################
def soundGraph(screenx, screeny, x, y):
    
    pygame.midi.init()                       #not initializing(increased gaps)reduces sound gaps
    player = pygame.midi.Output(0)
    
    screenXDim = []
    screenYDim = []
    e=0
    for col in range(12):
        screenXDim.append((screenx/12)*(col+1))
        for row in range(5):
            screenYDim.append((screeny/5)*(row+1))
            if  (x < (screenXDim[col]) and  y < (screenYDim[row])):
                e = 1
                break
        if e ==1:        
            break
 
    notes = [ 
            [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95],
            [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
            [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71],
            [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
            [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
            ]

    note = notes[row][col]
    
    print(note)
    
    player.set_instrument(0)
    player.note_on(note, 100)
    time.sleep(1)
    player.note_off(note, 100)
    
    del player
    pygame.midi.quit()
    

#############################################################################################    

if __name__ == "__main__":

    pyautogui.FAILSAFE = False
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 8)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    index_x, index_y = 0, 0
    pro = False
    while True:
        _, frame = cap.read()   
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame = cv2.GaussianBlur(rgb_frame,(5,5),0)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):

                    x = int(landmark.x*frame_width)
                    y = int(landmark.y*frame_height)

                    if id == 8:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        index_x = screen_width/frame_width*x
                        index_y = screen_height/frame_height*y   
                        
                        pyautogui.moveTo(index_x, index_y)

                        p = multiprocessing.Process(target = soundGraph,args= (screen_width, screen_height, index_x, index_y))
                        p.daemon = True
                        pro = True
                        p.start()
                        
        cv2.imshow('Virtual Mouse', frame)
        key = cv2.waitKey(1)
        


#############################################################################################    
