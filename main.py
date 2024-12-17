import pygame
import menu
import game

pygame.init()
pygame.display.set_caption('Jolly Jumpers')

menu_ui = menu.Menu()
result = menu_ui.start()

if result == 'start':
    game_ui = game.Game()
    game_ui.start()

pygame.quit()