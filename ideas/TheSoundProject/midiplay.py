import pygame.midi
import time

note = 84

pygame.midi.init()

player = pygame.midi.Output(0)
player.set_instrument(0)

player.note_on(note, 127)
time.sleep(3)
player.note_off(note, 127)
del player
pygame.midi.quit()
