import pygame
import player as pl
import enemy as en
from pygame.locals import *

pygame.init()
screen_width = 1200
screen_height = 700
tile_size = 50
fps = 60

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jolly Jumpers')

#load resource
bg_img = pygame.image.load('assets/images/background/cityskyline.png')

      
class World():
    def __init__(self, data, background):
        self.tile_list = []
        self.background = background
        self.enemy_group = pygame.sprite.Group()

        #load resources
        dirt = pygame.image.load('assets/images/objects/dirt.png')
        grass = pygame.image.load('assets/images/objects/grass.png')

        for row in range(len(data)):
            for col in range(len(data[row])):
                cell = data[row][col]
                block = None

                if cell == 1:
                    block = dirt
                elif cell == 2:
                    block = grass
                elif cell == 3:
                    enemy = en.Enemy(col * tile_size, row * tile_size + 15, tile_size - 15, tile_size - 15)
                    self.enemy_group.add(enemy)

                if block:
                    img = pygame.transform.scale(block, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x =  col * tile_size
                    img_rect.y =  row * tile_size
                    self.tile_list.append((img, img_rect))
    
    #grid - test mode
    def draw_grid(self):
        for line in range(int(screen_height/tile_size)):
            pygame.draw.line(screen, (255,255,255), (0, line * tile_size), (screen_width, line * tile_size))

        for line in range(int(screen_width/tile_size)):
            pygame.draw.line(screen, (255,255,255), (line * tile_size, 0), (line * tile_size, screen_height))

    def draw(self):
        screen.blit(bg_img, (0,0))
        self.enemy_group.draw(screen)
        for tile in self.tile_list:
            obj, rect = tile
            screen.blit(obj, rect)
            # pygame.draw.rect(screen, (0, 0, 255), rect, 2)

    def update(self):
        self.enemy_group.update()


#map obstacles
world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


world = World(world_data, bg_img)
player = pl.Player(100, screen_height - 130, 50, 80)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #draw assets
    world.draw()
    world.update()
    player.update(screen, world)

    world.draw_grid()
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()