import pygame
from core import *

pygame.init()
pygame.display.set_caption('Jolly Jumpers')

main_menu = menu.Menu()
if main_menu.start() == 'start':
    play_game = game.Game()
    print(play_game.start())

pygame.quit()