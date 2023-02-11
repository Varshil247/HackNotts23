import pygame.midi
import time

def soundGraph(screenx, screeny, x, y):
    screenXDim = []
    screenYDim = []

    for i in range(12):
        screenXDim.append((screenx/12)*i)
    for i in range(5):
        screenYDim.append((screeny/5)*i)

    for i in range(len(screenXDim)):
        if  x < ((screenx/12)*i):
            break

    for j in range(len(screenYDim)):
        if  y < ((screenx/5)*j):
            break
    
    soundNotes(5-j, i)

def soundNotes(row, col):
   notes = [ 
            [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95],
            [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
            [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71],
            [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
            [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
            ]

   playNote(notes[row][col])

def playNote(note):
    print(note)

    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(0)
    player.note_on(note, 127)
    player.note_off(note, 127)
    del player
    pygame.midi.quit()
