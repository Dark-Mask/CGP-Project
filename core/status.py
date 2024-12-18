import pygame

class GameStatus:
    def __init__(self, world):
        self.world = world
        self.health = 240
        self.total_pickup = len(world.collect_group)
        self.collected = 0
        self.time = 0
        self.shield = False

        self.health_img = pygame.image.load('assets/images/status/life.png')
        self.health_img = pygame.transform.scale(self.health_img, (350, 80))
        self.health_rect = self.health_img.get_rect()
        self.health_rect.x = 50
        self.health_rect.y = 20

        self.timer_img = pygame.image.load('assets/images/status/timer.png')
        self.timer_img = pygame.transform.scale(self.timer_img, (200, 80))
        self.timer_rect = self.timer_img.get_rect()
        self.timer_rect.x = 500
        self.timer_rect.y = 20

        self.collect_img = pygame.image.load('assets/images/status/collect.png')
        self.collect_img = pygame.transform.scale(self.collect_img, (200, 80))
        self.collect_rect = self.collect_img.get_rect()
        self.collect_rect.x = 800
        self.collect_rect.y = 20

        self.font = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 100)

        self.health_bar = pygame.Rect(self.health_rect.x+85, self.health_rect.y+20, self.health, 40)
        self.timer_display = (self.timer_rect.x+82, self.timer_rect.y+23)
        self.collect_display = (self.collect_rect.x+85, self.collect_rect.y+23)
        self.last_tick = pygame.time.get_ticks()


    def has_heatlh(self):
        return self.health > 0

    def has_completed(self):
        return self.collected == self.total_pickup

    def damage(self, damage):
        d_health = self.health - damage

        #apply damage when health is not zero
        if d_health <= 0:
            self.health = 0
        else:
            self.health = d_health
        self.health_bar.width = self.health    

    def item_collected(self):
        if self.collected < self.total_pickup:
            self.collected += 1

    def draw(self, screen):
        screen.blit(self.health_img, self.health_rect)
        screen.blit(self.timer_img, self.timer_rect)
        screen.blit(self.collect_img, self.collect_rect)

        #time and collection status
        minutes = self.time // 60
        seconds = self.time % 60
        screen.blit(self.font.render(f'{minutes:02}:{seconds:02}', True, (255,255,255)), self.timer_display)
        screen.blit(self.font.render(f'{self.collected}/{self.total_pickup}', True, (255,255,255)), self.collect_display)
        pygame.draw.rect(screen, (255,0,0), self.health_bar)

        #level complete text
        if self.has_completed():
            width, height = screen.get_size()
            text = self.font2.render(f'Level Complete', True, (192,192,192))
            text_rect = text.get_rect()
            text_rect.center = (width // 2, height // 2)
            screen.blit(text,  text_rect)

    def update(self):
        current_tick = pygame.time.get_ticks()

        if current_tick - self.last_tick > 1000:
            self.last_tick = current_tick
            self.time += 1