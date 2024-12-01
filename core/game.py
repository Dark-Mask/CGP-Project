import pygame, sys
from core import action, settings
from ui import menu as mnu
from utils import gravity
from components import player as pl
from components import map_forest, map_snow, map_undead
from pygame.locals import *

class Game:
    def __init__(self):
        #initialize pygame
        pygame.init()

        #screen configuration
        pygame.display.set_caption(settings.GAME_TITLE)
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HIGHT))

        #components
        self.player = pl.Player(self.screen.get_width() / 2, self.screen.get_height() / 2, 50, 50, 'red')

        #ui
        self.menu = mnu.Menu()

        #maps
        self.forest = map_forest.ForestMap()
        self.snow = map_snow.SnowMap()
        self.undead = map_undead.UndeadMap()

        #utils
        self.gravity = gravity.ObjectGravity(0.5, 0.8)

        self.isGameStart = False
        self.isRunning = True

    def start(self):
        #game loop
        while self.isRunning:
            self.screen.fill(settings.BACKGROUND_COLOR)

            #event handler
            py_events = pygame.event.get()
            action.close_game(py_events)

            if self.isGameStart:
                #handle movement event
                action.move_player(self.player)
                self.gravity.apply_gravity(self.player)

                #update character
                self.undead.draw(self.screen)
                self.player.draw(self.screen)

            else:
                #selecting game menu options
                action.select_menu(py_events, self.menu, self)

                #update menu
                self.menu.draw(self.screen)


            pygame.display.flip() #update screen
            pygame.time.Clock().tick(settings.FPS) #frame rate

        #terminate game
        pygame.quit()
        sys.exit()