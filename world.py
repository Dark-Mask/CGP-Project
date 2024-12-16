import pygame

#World Class
class World():
    def __init__(self, data, tile_size):
        self.enemy_group = pygame.sprite.Group()
        self.block_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

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
                elif cell == 4:
                    boss = Boss(col * tile_size, row * tile_size, self.bullet_group)
                    self.enemy_group.add(boss)

                if block:
                    img = pygame.transform.scale(block, (tile_size, tile_size))
                    block_tile = Block(col * tile_size, row * tile_size, img)
                    self.block_group.add(block_tile)

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.enemy_group.draw(screen)
        self.block_group.draw(screen)
        self.bullet_group.draw(screen)

    def update(self):
        print(self.bullet_group)
        self.bullet_group.update()
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


#Boss Class
class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.bullet_group = bullet_group
        self.image = pygame.Surface((50, 50))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.move_direction = 1
        self.move_counter = 0
        self.shoot_cooldown = 800  # Time between shots in milliseconds
        self.last_shot = pygame.time.get_ticks()

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_cooldown:
            self.last_shot = current_time

            # Fire multiple bullets in different directions
            directions = [
                (0, 5),  # Straight up
                (3, 4),  # Slightly left
                (-3, 4),   # Slightly right
            ]
            for dx, dy in directions:
                bullet = Bullet(self.rect.centerx, self.rect.centery, dx, dy)
                self.bullet_group.add(bullet)

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 40:
            self.move_direction *= -1
            self.move_counter *= -1
        self.shoot()


# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x=0, speed_y=-5):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.s_width, self.s_height = pygame.display.get_surface().get_size()

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Remove the bullet if it moves off-screen
        if self.rect.bottom < 0 or self.rect.top > self.s_height or self.rect.right < 0 or self.rect.left > self.s_width:
            self.kill()