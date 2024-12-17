import pygame
import components.minion as minion
import components.tile as tile
import components.boss as boss
import map.world as world

class World1(world.World):
    def __init__(self, map_data):
        super().__init__()

        #load world assets
        self.background = pygame.image.load('assets/images/background/cityskyline.png')
        mushroom = pygame.image.load('assets/images/objects/mushroom.png')
        dirt = pygame.image.load('assets/images/objects/dirt.png')
        grass = pygame.image.load('assets/images/objects/grass.png')

        for row in range(len(map_data)):
            for col in range(len(map_data[row])):
                #word map
                cell = map_data[row][col]
                block = None
                item = None
                temp_row = row
                temp_col = col
                
                if cell == 1:
                    block = dirt
                elif cell == 2:
                    block = grass
                elif cell == 3:
                    enemy_minion = minion.Minion(temp_col * self.tile_size, temp_row * self.tile_size + 15, self.tile_size - 15, self.tile_size - 15)
                    self.enemy_group.add(enemy_minion)
                elif cell == 4:
                    enemy_boss = boss.Boss(temp_col * self.tile_size, temp_row * self.tile_size, self.bullet_group)
                    self.enemy_group.add(enemy_boss)
                elif cell == 5:
                    item = mushroom
                elif cell == -1:
                    #shify block left
                    block = dirt
                    temp_col -= 1
                elif cell == -2:
                    #shify block right
                    block = dirt
                    temp_col += 1
                elif cell == -3:
                    #shify block up
                    block = dirt
                    temp_row -= 1
                elif cell == -4:
                    #shify block down
                    block = dirt
                    temp_row += 1

                if block:
                    img = pygame.transform.scale(block, (self.tile_size, self.tile_size))
                    block_tile = tile.Block(temp_col * self.tile_size, temp_row * self.tile_size, img)
                    self.block_group.add(block_tile)

                if item:
                    img = pygame.transform.scale(item, (self.tile_size-15, self.tile_size-15))
                    collect_item = tile.Block(temp_col * self.tile_size, temp_row * self.tile_size+15, img)
                    self.collect_group.add(collect_item)