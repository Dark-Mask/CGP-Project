import pygame, sys
from core import event, setting
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
        pygame.display.set_caption(setting.GAME_TITLE)
        self.screen = pygame.display.set_mode((setting.SCREEN_WIDTH, setting.SCREEN_HIGHT))

        #components
        self.player = pl.Player(self.screen.get_width() / 2, 10, 50, 50, 'red')
        self.forest = map_forest.ForestMap()
        self.snow = map_snow.SnowMap()
        self.undead = map_undead.UndeadMap()

        #ui
        self.menu = mnu.Menu()

        #utils
        self.gravity = gravity.ObjectGravity(0.5)

        self.isGameStart = False
        self.isRunning = True

    def start(self):
        #game loop
        while self.isRunning:
            self.screen.fill(setting.BACKGROUND_COLOR)

            #event handler
            py_events = pygame.event.get()
            event.close_game(py_events)

            if self.isGameStart:
                #handle movement event
                event.move_object(self.player)
                self.gravity.apply_gravity(self.player)

                #update character
                self.snow.draw(self.screen)
                self.player.draw(self.screen)

            else:
                #selecting game menu options
                event.select_menu(py_events, self.menu, self)

                #update menu
                self.menu.draw(self.screen)


            pygame.display.flip() #update screen
            pygame.time.Clock().tick(setting.FPS) #frame rate

        #terminate game
        pygame.quit()
        sys.exit()