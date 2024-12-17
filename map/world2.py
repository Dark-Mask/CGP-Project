import pygame
import map.world as world


class World1(world.World):
    def __init__(self, map_data):
        #load world assets
        background = pygame.image.load('assets/images/background/cityskyline.png')
        ground = pygame.image.load('assets/images/objects/dirt.png')
        platform = pygame.image.load('assets/images/objects/grass.png')
        pickup = pygame.image.load('assets/images/objects/mushroom.png')
        minion = pygame.image.load('assets/images/enemy/snowman.png')
        boss = pygame.image.load('assets/images/enemy/snowman.png')
        super().__init__(map_data, background, ground, platform, pickup, minion, boss)
        
