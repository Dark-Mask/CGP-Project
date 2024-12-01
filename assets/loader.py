import pygame

def menu_ui():
    return pygame.image.load('assets/images/menu.png')

def background(background):
    if background == 'forest':
        return pygame.image.load('assets/images/background/forest.png')
    elif background == 'snow':
        return pygame.image.load('assets/images/background/snow.png')
    elif background == 'undead':
        return pygame.image.load('assets/images/background/undead.png')
    elif background == 'sky':
        return pygame.image.load('assets/images/background/cityskyline.png')