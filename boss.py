import pygame
import bullet as blt

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
                (3, 4),  # Slightly right
                (-3, 4)   # Slightly left
            ]
            for dx, dy in directions:
                bullet = blt.Bullet(self.rect.centerx, self.rect.centery, dx, dy)
                self.bullet_group.add(bullet)

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 40:
            self.move_direction *= -1
            self.move_counter *= -1
        self.shoot()

