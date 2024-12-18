import pygame
from core import *

pygame.init()
pygame.display.set_caption('Jolly Jumpers')

main_menu = menu.Menu()
if main_menu.run() == 'start':
    play_game = game.Game()
    game_manager = play_game.start()

    if game_manager.is_gameover():
        print('Play: gameover')
    else:
        print('Play: winner')
    
    print(f'time: {game_manager.final_time()}')
    print(f'collected: {game_manager.final_collection()}')

pygame.quit()