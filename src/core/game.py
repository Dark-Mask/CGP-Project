from core import settings, events
import sys
import pygame
from pygame.locals import *

def start():
    #initialize pygame
    pygame.init()

    #screen configuration
    pygame.display.set_caption(settings.GAME_TITLE)
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HIGHT))


    #game loop
    while True:
        screen.fill(settings.BACKGROUND_COLOR)

        #event handler
        events.handle_event()

        #update screen
        pygame.display.update()

        #frame rate
        pygame.time.Clock().tick(settings.FPS)