import pygame

#World Class
class World():
    def __init__(self, data, tile_size):
        self.enemy_group = pygame.sprite.Group()
        self.block_group = pygame.sprite.Group()

        #load world assets
        self.background = pygame.image.load('assets/images/background/cityskyline.png')
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
                    enemy = Enemy(col * tile_size, row * tile_size + 15, tile_size - 15, tile_size - 15)
                    self.enemy_group.add(enemy)

                if block:
                    img = pygame.transform.scale(block, (tile_size, tile_size))
                    block_tile = Block(col * tile_size, row * tile_size, img)
                    self.block_group.add(block_tile)

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.enemy_group.draw(screen)
        self.block_group.draw(screen)

    def update(self):
        self.enemy_group.update()


#Block Class
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


#Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load('assets/images/enemy/snowman.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 40:
            self.move_direction *= -1
            self.move_counter *= -1