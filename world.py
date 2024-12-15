import pygame

class World():
    def __init__(self, data, screen, tile_size):
        self.screen = screen
        self.tile_size = tile_size
        self.tile_list = []

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

                if block:
                    img = pygame.transform.scale(block, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x =  col * self.tile_size
                    img_rect.y =  row * self.tile_size
                    self.tile_list.append((img, img_rect))
    
    #grid - test mode
    def draw_grid(self):
        for line in range(int(self.screen.get_height()/self.tile_size)):
            pygame.draw.line(self.screen, (255,255,255), (0, line * self.tile_size), (self.screen.get_width(), line * self.tile_size))

        for line in range(int(self.screen.get_width()/self.tile_size)):
            pygame.draw.line(self.screen, (255,255,255), (line * self.tile_size, 0), (line * self.tile_size, self.screen.get_height()))


    def draw(self):
        for tile in self.tile_list:
            obj, rect = tile
            self.screen.blit(obj, rect)
            pygame.draw.rect(self.screen, (0, 0, 255), rect, 2)