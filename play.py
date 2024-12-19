import pygame, sys
from core import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Jolly Jumpers')

running = True
restart = False
while running:

    if not restart:
        main_menu = menu.Menu()

        if not main_menu.run():
            break

    play_game = game.Game()
    game_manager = play_game.start()

    if game_manager.is_shutdown():
        break

    if game_manager.is_gameover():
        loss_game = gameover.GameOver(game_manager)
        running = loss_game.run()
        restart = True
    else:
        win_game = winner.Winner(game_manager)
        running = win_game.run()
        restart = False


pygame.quit()
sys.exit()