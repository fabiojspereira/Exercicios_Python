import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('som.mp3')
pygame.mixer.music.play()
#pygame.mixer.music.set_volume()
pygame.event.wait()

stop = str(input("Press ENTER to stop music ... "))