import pygame, sys
from core import *

pygame.init()
pygame.display.set_caption('Jolly Jumpers')

main_menu = menu.Menu()
play_game = game.Game()
loss_game = gameover.GameOver()
win_game = winner.Winner()

if main_menu.run() == 'start':
    game_manager = play_game.start()

    if game_manager.is_shutdown():
        pygame.quit()
        sys.exit()

    if game_manager.is_gameover():
        loss_game.start()
    else:
        win_game.start()
    
    print(f'time: {game_manager.final_time()}')
    print(f'collected: {game_manager.final_collection()}')

pygame.quit()