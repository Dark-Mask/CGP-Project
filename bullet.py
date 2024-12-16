import pygame

# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction_x=0, direction_y=-5):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.s_width, self.s_height = pygame.display.get_surface().get_size()

    def update(self):

        self.rect.x += self.direction_x
        self.rect.y += self.direction_y
        # Remove the bullet if it moves off-screen
        if self.rect.bottom < 0 or self.rect.top > self.s_height or self.rect.right < 0 or self.rect.left > self.s_width:
            self.kill()