import pygame
import components.minion as minion
import components.block as block
import components.item as item
import components.boss as boss

#use in game
GROUND = 1
PLATFORM = 2
PICKUP = 3
ENEMY_MINION = 4
ENEMY_BOSS = 5

#use for border only
SHIFT_LEFT = -1
SHIFT_RIGHT = -2
SHIFT_UP = -3
SHIFT_DOWN = -4

#World Class
class World():
    def __init__(self, map_data, background, ground, platform, pickup, minion, boss):
        self.width = 1200
        self.height = 700
        self.tile_size = 30
        self.reduce_tile_size = self.tile_size * 0.1
        self.map_data = map_data
        
        self.enemy_group = pygame.sprite.Group()
        self.collect_group = pygame.sprite.Group()
        self.block_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        self.background = background
        self.ground = ground
        self.platform = platform
        self.pickup = pickup
        self.minion = minion
        self.boss = boss

        self._load_map()

    def _load_map(self):
        for row in range(len(self.map_data)):
            for col in range(len(self.map_data[row])):
                #word map_data
                cell = self.map_data[row][col]
                temp_col, temp_row = (col, row)
                
                #modify row and column value if shift used
                if cell in (SHIFT_LEFT, SHIFT_RIGHT, SHIFT_UP, SHIFT_DOWN):
                    temp_col, temp_row = self._calculate_shift(cell, temp_col, temp_row)
                    cell = GROUND

                #add object to world
                if cell == GROUND:
                    self._add_block(self.ground, temp_col, temp_row)
                elif cell == PLATFORM:
                    self._add_block(self.platform, temp_col, temp_row)
                elif cell == PICKUP:
                    self._add_item(self.pickup, temp_col, temp_row)
                elif cell == ENEMY_MINION:
                    self._add_minion(self.minion, temp_col, temp_row)
                elif cell == ENEMY_BOSS:
                    self._add_boss(self.boss, temp_col, temp_row)
                

    def _calculate_shift(self, shift, col, row):
        if shift == SHIFT_LEFT:
            col -= 1
        elif shift == SHIFT_RIGHT:
            col += 1
        elif shift == SHIFT_UP:
            row -= 1
        elif shift == SHIFT_DOWN:
            row += 1
        
        return (col, row)


    def _add_block(self, image, col, row):
        image = pygame.transform.scale(image, (self.tile_size, self.tile_size))
        world_block = block.Block(image, col * self.tile_size, row * self.tile_size)
        self.block_group.add(world_block)


    def _add_item(self, image, col, row):
        image = pygame.transform.scale(image, (self.tile_size - self.reduce_tile_size , self.tile_size - self.reduce_tile_size))
        world_item = item.Item(image, col * self.tile_size, row * self.tile_size + self.reduce_tile_size, self)
        self.collect_group.add(world_item)


    def _add_minion(self, image, col, row):
        image = pygame.transform.scale(image, (self.tile_size - self.reduce_tile_size, self.tile_size - self.reduce_tile_size))
        world_minion = minion.Minion(image, col * self.tile_size, row * self.tile_size + self.reduce_tile_size, self)
        self.enemy_group.add(world_minion)


    def _add_boss(self, image, col, row):
        image = pygame.transform.scale(image, (self.tile_size + self.reduce_tile_size, self.tile_size + self.reduce_tile_size))
        world_boss = boss.Boss(image, col * self.tile_size, row * self.tile_size - (self.reduce_tile_size + self.reduce_tile_size * 0.5), self.bullet_group)
        self.enemy_group.add(world_boss)


    def draw_grid(self, screen):
        for line in range(int(self.height/self.tile_size)):
            pygame.draw.line(screen, (255,255,255), (0, line * self.tile_size), (self.width, line * self.tile_size))

        for line in range(int(self.width/self.tile_size)):
            pygame.draw.line(screen, (255,255,255), (line * self.tile_size, 0), (line * self.tile_size, self.height))


    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.collect_group.draw(screen)
        self.block_group.draw(screen)
        self.enemy_group.draw(screen)
        self.bullet_group.draw(screen)


    def update(self):
        self.bullet_group.update()
        self.enemy_group.update()
        self.collect_group.update()





