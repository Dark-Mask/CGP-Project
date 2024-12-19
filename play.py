import pygame, sys
from core import *

pygame.init()
pygame.display.set_caption('Jolly Jumpers')

main_menu = menu.Menu()
play_game = game.Game()

running = True
while running:
    if main_menu.run() == 'start':
        game_manager = play_game.start()

        if game_manager.is_shutdown():
            pygame.quit()
            sys.exit()

        if game_manager.is_gameover():
            loss_game = gameover.GameOver(game_manager)
            running = loss_game.run()
        else:
            win_game = winner.Winner(game_manager)
            running = win_game.run()
    else:
        running = False

pygame.quit()