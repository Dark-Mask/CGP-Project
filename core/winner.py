import pygame

class Winner:
    def __init__(self, game_manager):
        self.width = 800
        self.height = 600

        self.background = pygame.image.load('assets/images/background/cityskyline.png')
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.summary = pygame.image.load('assets/images/winner.png')
        self.summary = pygame.transform.scale(self.summary, (550, 500))

        self.options = [('Start', (170, 320)), ('Quit', (180, 420))]
        self.font = pygame.font.Font(None, 70)
        self.color = pygame.color.Color(240, 240, 240)

        self.display_time = self.format_time(game_manager.final_time())
        self.display_collection = game_manager.final_collection()

    
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
        screen.blit(self.font.render(f'{self.display_time}', True, self.color), (center_x, center_y))
            

    def start(self, fps=60):
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Jolly Jumpers - Winner')
        clock = pygame.time.Clock()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw(screen)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                run = False
                

            pygame.display.update()
            clock.tick(fps)
        
        #close window
        pygame.display.quit()

