import pygame
from pygame.locals import *
import minion, tile, boss

#World Class
class World():
    def __init__(self, data):
        self.width = 1200
        self.height = 700
        self.tile_size = 40

        self.enemy_group = pygame.sprite.Group()
        self.item_group = pygame.sprite.Group()
        self.block_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        #load world assets
        self.background = pygame.image.load('assets/images/background/cityskyline.png')
        dirt = pygame.image.load('assets/images/objects/dirt.png')
        grass = pygame.image.load('assets/images/objects/grass.png')

        for row in range(len(data)):
            for col in range(len(data[row])):
                #word map
                cell = data[row][col]
                block = None

                if cell == 1:
                    block = dirt
                elif cell == 2:
                    block = grass
                elif cell == 3:
                    enemy_minion = minion.Minion(col * self.tile_size, row * self.tile_size + 15, self.tile_size - 15, self.tile_size - 15)
                    self.enemy_group.add(enemy_minion)
                elif cell == 4:
                    enemy_boss = boss.Boss(col * self.tile_size, row * self.tile_size, self.bullet_group)
                    self.enemy_group.add(enemy_boss)

                if block:
                    img = pygame.transform.scale(block, (self.tile_size, self.tile_size))
                    block_tile = tile.Block(col * self.tile_size, row * self.tile_size, img)
                    self.block_group.add(block_tile)


    def draw_grid(self, screen):
        for line in range(int(self.height/self.tile_size)):
            pygame.draw.line(screen, (255,255,255), (0, line * self.tile_size), (self.width, line * self.tile_size))

        for line in range(int(self.width/self.tile_size)):
            pygame.draw.line(screen, (255,255,255), (line * self.tile_size, 0), (line * self.tile_size, self.height))


    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.enemy_group.draw(screen)
        self.block_group.draw(screen)
        self.bullet_group.draw(screen)


    def update(self):
        self.bullet_group.update()
        self.enemy_group.update()





