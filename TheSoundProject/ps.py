import cv2
import mediapipe as mp
import pyautogui
import pygame.midi
import numpy as np
import time
import multiprocessing
#import rtmidi

def play_sound(note):
    pygame.midi.init()                       #not initializing(increased gaps)reduces sound gaps
    player = pygame.midi.Output(0)

    player.set_instrument(0)
    player.note_on(note, 100)
    time.sleep(1)
    player.note_off(note, 100)
    
    del player
    pygame.midi.quit()