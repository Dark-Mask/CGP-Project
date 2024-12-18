import pygame
import world.world as world

class Cemetery(world.World):
    def __init__(self, map_data):
        #load world assets
        backgroun_music = 'assets/sounds/background_music.mp3'
        background = pygame.image.load('assets/images/background/cementery.png')
        ground = pygame.image.load('assets/images/objects/dirt.png')
        platform = pygame.image.load('assets/images/objects/grave.png')
        pickup = pygame.image.load('assets/images/objects/mushroom.png')
        minion = pygame.image.load('assets/images/enemy/reaper_ghost.png')
        boss = pygame.image.load('assets/images/enemy/boss_ghoul.png')
        super().__init__(map_data, background, backgroun_music, ground, platform, pickup, minion, boss)
        
    
class Forest(world.World):
    def __init__(self, map_data):
        #load world assets
        backgroun_music = 'assets/sounds/background_music.mp3'
        background = pygame.image.load('assets/images/background/cityskyline.png')
        ground = pygame.image.load('assets/images/objects/dirt.png')
        platform = pygame.image.load('assets/images/objects/grass.png')
        pickup = pygame.image.load('assets/images/objects/mushroom.png')
        minion = pygame.image.load('assets/images/enemy/forest_mushroom.png')
        boss = pygame.image.load('assets/images/enemy/boss_tree.png')
        super().__init__(map_data, background, backgroun_music, ground, platform, pickup, minion, boss)


class Snow(world.World):
    def __init__(self, map_data):
        #load world assets
        backgroun_music = 'assets/sounds/background_music.mp3'
        background = pygame.image.load('assets/images/background/snow.png')
        ground = pygame.image.load('assets/images/objects/dirt.png')
        platform = pygame.image.load('assets/images/objects/snow.png')
        pickup = pygame.image.load('assets/images/objects/mushroom.png')
        minion = pygame.image.load('assets/images/enemy/snowman.png')
        boss = pygame.image.load('assets/images/enemy/boss_golem.png')
        super().__init__(map_data, background, backgroun_music, ground, platform, pickup, minion, boss)
