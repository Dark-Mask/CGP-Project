import pygame

class Player:

    # constructor
    def __init__(self, x, y, width, height, color):
        self.position = pygame.Vector2(x, y)
        self.width = width
        self.height = height
        self.color = color
        self.radius = 10
        self.collider = pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2, self.radius * 2)

    # update position
    def move(self, dx=0, dy=0):
        self.position += pygame.Vector2(dx, dy)

    def collider_box(self):
        return self.collider

    #draw player
    def draw(self, screen):
        self.collider = pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2, self.radius * 2)
        pygame.draw.circle(screen, self.color, self.position,  self.radius)