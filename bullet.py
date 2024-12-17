import pygame

# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x=0, velocity_y=-5):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.s_width, self.s_height = pygame.display.get_surface().get_size()
        self.last_tick = pygame.time.get_ticks()
        self.bullet_speed = 1 #millis (lower value make fast bullet)

    def update(self):
        current_tick = pygame.time.get_ticks()

        if current_tick - self.last_tick > self.bullet_speed:
            self.last_tick = current_tick
            self.rect.x += self.velocity_x
            self.rect.y += self.velocity_y
            
        # Remove the bullet if it moves off-screen
        if self.rect.bottom < 0 or self.rect.top > self.s_height or self.rect.right < 0 or self.rect.left > self.s_width:
            self.kill()