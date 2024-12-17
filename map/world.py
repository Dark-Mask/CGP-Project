import pygame
from pygame.locals import *

#World Class
class World():
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.tile_size = 40
        
        self.enemy_group = pygame.sprite.Group()
        self.collect_group = pygame.sprite.Group()
        self.block_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()


    def draw_grid(self, screen):
        for line in range(int(self.height/self.tile_size)):
            pygame.draw.line(screen, (255,255,255), (0, line * self.tile_size), (self.width, line * self.tile_size))

        for line in range(int(self.width/self.tile_size)):
            pygame.draw.line(screen, (255,255,255), (line * self.tile_size, 0), (line * self.tile_size, self.height))


    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.collect_group.draw(screen)
        self.enemy_group.draw(screen)
        self.block_group.draw(screen)
        self.bullet_group.draw(screen)


    def update(self):
        self.bullet_group.update()
        self.enemy_group.update()





