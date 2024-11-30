import pygame

class Player:

    # constructor
    def __init__(self, x, y, width, height, color):
        self.position = pygame.Vector2(x, y)
        self.width = width
        self.height = height
        self.color = color

    # update position
    def move(self, dx, dy):
        self.position += pygame.Vector2(dx, dy)


    #draw player
    def draw(self, screen):
         pygame.draw.circle(screen, self.color, self.position, 40)