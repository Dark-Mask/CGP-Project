import pygame

#Block Class
class Item(pygame.sprite.Sprite):
    def __init__(self, image, x, y, world):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.world = world
        self.velocity = 0

    def update(self):
        #temporary store movement change before applying
        delta_x = 0
        delta_y = 0

        self.velocity += 1 #gravity fall
        if self.velocity > 10: #peak velocity
            self.velocity = 10
        delta_y += self.velocity

        #world collision
        self.rect.x += delta_x #x-direction collision
        if pygame.sprite.spritecollide(self, self.world.block_group, False):
            self.rect.x -= delta_x #don't apply movement on wall collision
        
        self.rect.y += delta_y #y-direction collision
        if pygame.sprite.spritecollide(self, self.world.block_group, False):
            self.rect.y -= delta_y #don't apply movement on ground collision     
            self.velocity = 0  
