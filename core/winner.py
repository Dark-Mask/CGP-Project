import pygame, sys

class Winner:
    def __init__(self, game_manager):
        self.width = 800
        self.height = 600

        self.winner_effect = pygame.mixer.Sound('assets/sounds/winner_effect.mp3')
        self.background = pygame.image.load('assets/images/background/cityskyline.png')
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.summary = pygame.image.load('assets/images/winner.png')
        self.summary = pygame.transform.scale(self.summary, (380, 550))

        self.game_summary = [(self.format_time(game_manager.final_time()), (170, 255)), (str(game_manager.final_collection()), (170, 325))]
        self.font = pygame.font.Font(None, 45)
        self.color = pygame.color.Color(240, 240, 240)

    
    def format_time(self, time):
        minutes = time // 60
        seconds = time % 60

        return f'{minutes:02}:{seconds:02}'

    def draw(self, screen):
        center_x = (self.width - self.summary.get_width()) // 2
        center_y = (self.height - self.summary.get_height()) // 2

        #menu background
        screen.blit(self.background, (0, 0))
        screen.blit(self.summary, (center_x, center_y))

        #draw options
        for content in self.game_summary:
            text, coord = content
            screen.blit(self.font.render(text, True, self.color), (center_x+coord[0], center_y+coord[1]))
            

    def run(self, fps=60):
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        pygame.display.set_caption('Jolly Jumpers - Winner')
        self.winner_effect.play()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw(screen)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                run = False
                

            pygame.display.update()
            clock.tick(fps)
        
        #close window
        pygame.mixer.stop()
        pygame.display.quit()
        return True

