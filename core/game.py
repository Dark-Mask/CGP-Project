import pygame
from core import settings, events
from ui import menu
from components import player
from pygame.locals import *

def start():
    #initialize pygame
    pygame.init()

    #screen configuration
    pygame.display.set_caption(settings.GAME_TITLE)
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HIGHT))

    #entity
    hero = player.Player(screen.get_width() / 2, screen.get_height() / 2, 50, 50, 'red')
    game_menu = menu.Menu()

    isGameStart = False
    #game loop
    while True:
        screen.fill(settings.BACKGROUND_COLOR)

        # event handler
        events.exit_event()

        if isGameStart:
            pass
        else:
            events.selection_event(game_menu)
            game_menu.draw(screen)


        pygame.display.flip() #update screen
        pygame.time.Clock().tick(settings.FPS) #frame rate