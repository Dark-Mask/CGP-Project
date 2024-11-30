import pygame
from assets import loader

class ForestMap:

    #constructor
    def __init__(self):
        self.background = pygame.transform.scale(loader.game_map('forest'), (800, 600))


    def draw(self, screen):
        #background
        screen.blit(self.background, (0, 0))