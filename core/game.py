from core import settings, events
from components import player
import pygame
from pygame.locals import *

def start():
    #initialize pygame
    pygame.init()

    #screen configuration
    pygame.display.set_caption(settings.GAME_TITLE)
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HIGHT))

    #entity
    hero = player.Player(screen.get_width() / 2, screen.get_height() / 2, 50, 50, 'red')


    #game loop
    while True:
        screen.fill(settings.BACKGROUND_COLOR)

        #event handler
        events.exit_event()
        events.movement_event(hero)

        #draw hero
        hero.draw(screen)

        #update screen
        pygame.display.flip()

        #frame rate
        pygame.time.Clock().tick(settings.FPS)