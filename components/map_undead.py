import pygame
from assets import loader

class UndeadMap:

    #constructor
    def __init__(self):
        self.background = pygame.transform.scale(loader.game_map('undead'), (800, 600))


    def draw(self, screen):
        #background
        screen.blit(self.background, (0, 0))