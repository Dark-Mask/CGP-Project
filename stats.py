import pygame

class GameStat:
    def __init__(self):
        self.health = 240
        self.points = 0
        self.time = 0
        self.shield = False

        self.health_img = pygame.image.load('assets/images/stats/life.png')
        self.health_img = pygame.transform.scale(self.health_img, (350, 80))
        self.health_rect = self.health_img.get_rect()
        self.health_rect.x = 50
        self.health_rect.y = 20

        self.timer_img = pygame.image.load('assets/images/stats/timer.png')
        self.timer_img = pygame.transform.scale(self.timer_img, (200, 80))
        self.timer_rect = self.timer_img.get_rect()
        self.timer_rect.x = 500
        self.timer_rect.y = 20

        self.point_img = pygame.image.load('assets/images/stats/point.png')
        self.point_img = pygame.transform.scale(self.point_img, (200, 80))
        self.point_rect = self.point_img.get_rect()
        self.point_rect.x = 800
        self.point_rect.y = 20

        self.font = pygame.font.Font(None, 50)
        self.health_bar = pygame.Rect(self.health_rect.x+85, self.health_rect.y+20, self.health, 40)
        self.timer_display = (self.timer_rect.x+82, self.timer_rect.y+23)
        self.last_tick = pygame.time.get_ticks()


    def damage(self, damage):
        d_health = self.health - damage

        #apply damage when health is not zero
        if d_health >= 0:
            if d_health <= 0:
                self.health = 0
            else:
                self.health = d_health
            self.health_bar.width = self.health

    def point(self, point):
        self.point += point

    def draw(self, screen):
        screen.blit(self.health_img, self.health_rect)
        screen.blit(self.timer_img, self.timer_rect)
        screen.blit(self.point_img, self.point_rect)

        #format time
        minutes = self.time // 60
        seconds = self.time % 60
        screen.blit(self.font.render(f'{minutes:02}:{seconds:02}', True, (255,255,255)), self.timer_display)
        pygame.draw.rect(screen, (255,0,0), self.health_bar)

    def update(self):
        current_tick = pygame.time.get_ticks()

        if current_tick - self.last_tick > 1000:
            self.last_tick = current_tick
            self.time += 1