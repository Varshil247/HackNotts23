import cv2
import mediapipe as mp
import pyautogui
#capure video live
pyautogui.FAILSAFE = False
cap = cv2.VideoCapture(0)
# detect
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
#get screeen
screen_width, screen_height = pyautogui.size()
#set start
index_y = 0

while True:
    _, frame = cap.read() #read    

    frame = cv2.flip(frame, 1) 
    frame_height, frame_width, _ = frame.shape
    #change color
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    #landmarks
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                #landmark coordinat 
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                #index
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    
                if id == 6:
                    index_xh = screen_width/frame_width*x
                    index_yh = screen_height/frame_height*y
                    
                if id == 9:
                    midbo_x = screen_width/frame_width*x
                    midbo_y = screen_height/frame_height*y
                    
                #thumb
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                 #mid   
                if id == 10:
                    mid_xh = screen_width/frame_width*x
                    mid_yh = screen_height/frame_height*y
                    
                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    mid_x = screen_width/frame_width*x
                    mid_y = screen_height/frame_height*y
                
                   # print('outside', abs(index_y - mid_y))
                    if abs(index_y - index_yh) < 15:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        
                    if abs(mid_y - mid_yh) < 20:
                        pyautogui.rightClick()
                        pyautogui.sleep(1)
                        
                    if  (abs(index_y - mid_y) < 100):
                        pyautogui.moveTo(index_x, index_y)
                        
                    if (abs(index_y - mid_y) < 22):
                        pyautogui.doubleClick()
                        pyautogui.sleep(1)
                        
                    if (abs(thumb_y - index_yh) < 25):
                        pyautogui.scroll(-120)
                        pyautogui.sleep(1)
                        
                    if (abs(thumb_y - midbo_y) < 25): 
                        pyautogui.scroll(120)
                        pyautogui.sleep(1)
                   
    
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)