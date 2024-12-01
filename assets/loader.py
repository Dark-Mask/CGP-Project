import pygame

def menu_ui():
    return pygame.image.load('assets/images/menu.png')

def menu_background():
    return pygame.image.load('assets/images/background/cityskyline.png')

def game_map(map):
    if map == 'forest':
        return pygame.image.load('assets/images/background/forest.png')
    elif map == 'snow':
        return pygame.image.load('assets/images/background/snow.png')
    elif map == 'undead':
        return pygame.image.load('assets/images/background/undead.png')