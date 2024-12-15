class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.shoot_cooldown = 1000  # Time between shots in milliseconds
        self.last_shot = pygame.time.get_ticks()

    def shoot(self, bullet_group):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_cooldown:
            self.last_shot = current_time

            # Fire multiple bullets in different directions
            directions = [
                (0, -5),  # Straight up
                (-3, -4),  # Slightly left
                (3, -4),   # Slightly right
            ]
            for dx, dy in directions:
                bullet = Bullet(self.rect.centerx, self.rect.centery, dx, dy)
                bullet_group.add(bullet)

    def update(self, bullet_group):
        self.shoot(bullet_group)



        # Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x=0, speed_y=-5):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Remove the bullet if it moves off-screen
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()