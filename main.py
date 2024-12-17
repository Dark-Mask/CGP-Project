import pygame
import menu
import game

pygame.init()
pygame.display.set_caption('Jolly Jumpers')

main_menu = menu.Menu()
if main_menu.start() == 'start':
    game_ui = game.Game()
    game_ui.start()

pygame.quit()