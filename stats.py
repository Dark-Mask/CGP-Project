import pygame

class GameStat:
    def __init__(self):
        self.health = 100
        self.points = 0
        self.shield = False

        self.health_img = pygame.image.load('assets/images/stats/life.png')
        self.health_img = pygame.transform.scale(self.health_img, (350, 80))
        self.point_img = pygame.image.load('assets/images/stats/point.png')
        self.point_img = pygame.transform.scale(self.point_img, (200, 80))
        self.timer_img = pygame.image.load('assets/images/stats/timer.png')
        self.timer_img = pygame.transform.scale(self.timer_img, (200, 80))

    def damage(self, damage):
        self.health -= damage

    def point(self, point):
        self.point += point

    def draw(self, screen):
        screen.blit(self.health_img, (50, 20))
        screen.blit(self.timer_img, (500, 20))
        screen.blit(self.point_img, (800, 20))

    def update(self):
        pass