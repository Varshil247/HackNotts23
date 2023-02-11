import cv2
import mediapipe as mp
import pyautogui
import time
import rtmidi

#############################################################################################    

def main():
    track()

############################################################################################# 
  
def track():
    pyautogui.FAILSAFE = False
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 12)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    index_x, index_y = 0, 0
    
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
                            
                        if (index_x and index_y):
                            pyautogui.moveTo(index_x, index_y)
                            soundGraph(screen_width, screen_height, index_x, index_y)

        cv2.imshow('Virtual Mouse', frame)
        cv2.waitKey(1)

#############################################################################################    

def soundGraph(screenx, screeny, x, y):
    screenXDim = []
    screenYDim = []

    for col in range(12):
        screenXDim.append((screenx/12)*(col+1))
        if  x < (screenXDim[col]):
            break

    for row in range(5):
        screenYDim.append((screeny/5)*(row+1))
        if  y < (screenYDim[row]):
            break
    
    soundNotes(row, col)

#############################################################################################   
 
def soundNotes(row, col):
    notes = [ 
            [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95],
            [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
            [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71],
            [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
            [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
            ]

    note = notes[row][col]
    playNote(note)

############################################################################################# 
   
def playNote(note):
    print(note)
    
    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()

    if available_ports:
        midiout.open_port(0)
    else:
        midiout.open_virtual_port("My virtual output")

    with midiout:
        note_on = [0x90, note, 127] # channel 1, middle C, velocity 112
        note_off = [0x80, note, 0]
        midiout.send_message(note_on)
        time.sleep(0.5)
        midiout.send_message(note_off)

    del midiout
    #pygame.midi.init()
    #player = pygame.midi.Output(0)
    #player.set_instrument(0)
    #player.note_on(note, 127)
    #time.sleep(1)
    #player.note_off(note, 127)
    #del player
    #pygame.midi.quit()

#############################################################################################    

if __name__ == "__main__":
    main()