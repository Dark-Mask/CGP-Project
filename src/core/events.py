import pygame
import sys

def handle_event():
    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print('a is pressed')