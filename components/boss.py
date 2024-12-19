import pygame
import components.bullet as bullet

#Boss Class
class Boss(pygame.sprite.Sprite):
    def __init__(self, image, x, y, bullet_group):
        super().__init__()
        self.shoot_effect = pygame.mixer.Sound('assets/sounds/shooting_effect.mp3')
        self.shoot_effect.set_volume(0.1)
        self.bullet_group = bullet_group
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.move_direction = 1
        self.move_counter = 0
        self.shoot_cooldown = 1000  # Time between shots in milliseconds
        self.last_shot = pygame.time.get_ticks()

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_cooldown:
            self.last_shot = current_time

            # Fire multiple bullets in different directions
            directions = [
                (0, 5),  # Straight down
                (2, 4),  # 1st right
                (4, 3),  # 2nd right
                (-2, 4), # 1st left
                (-4, 3), # 2nd right
            ]
            for dx, dy in directions:
                ammo = pygame.Surface((self.rect.width * 0.2, self.rect.height * 0.2))
                ammo.fill((255,0,0))
                boss_bullet = bullet.Bullet(ammo, self.rect.centerx, self.rect.centery, dx, dy)
                self.bullet_group.add(boss_bullet)
                self.shoot_effect.play()

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 40:
            self.move_direction *= -1
            self.move_counter *= -1
        self.shoot()

