import pygame

def get_menu():
    return pygame.image.load('assets/images/menu.png')

def menu_background():
    return pygame.image.load('assets/images/map/cityskyline.png')

def game_map(map):
    if map == 'forest':
        return pygame.image.load('assets/images/map/forest.png')
    elif map == 'snow':
        return pygame.image.load('assets/images/map/snow.png')
    elif map == 'cemetery':
        return pygame.image.load('assets/images/map/cemetery.png')