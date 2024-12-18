import pygame
from core import *

pygame.init()
pygame.display.set_caption('Jolly Jumpers')

main_menu = menu.Menu()
if main_menu.run() == 'start':
    play_game = game.Game()
    game_status = play_game.start()

    if game_status == 'gameover':
        print('Play: gameover')
    elif game_status == 'winner':
        print('Play: winner')

pygame.quit()