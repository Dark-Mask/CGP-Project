import pygame, sys

class Menu:
    def __init__(self):
        self.width = 800
        self.height = 600

        self.img = pygame.image.load('assets/images/background/cityskyline.png')
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.menu = pygame.image.load('assets/images/menu.png')
        self.menu = pygame.transform.scale(self.menu, (450, 500))


        self.options = [('Start', (170, 320)), ('Quit', (180, 420))]
        self.font = pygame.font.Font(None, 70)
        self.color = pygame.color.Color(240, 240, 240)
        self.select_cooldown = 50 #millis
        self.last_tick = pygame.time.get_ticks()
        self.selected = 0

    def get_selection(self):
        return self.selected == 0

    def draw(self, screen):
        menu_center_x = (self.width - self.menu.get_width()) // 2
        menu_center_y = (self.height - self.menu.get_height()) // 2

        #menu background
        screen.blit(self.img, (0, 0))
        screen.blit(self.menu, (menu_center_x, menu_center_y))

        #draw options
        for i in range(len(self.options)):
            text, coordinate = self.options[i]

            #highligh selection
            if i == self.selected:
                color = pygame.color.Color(255, 63, 141)
            else:
                color = self.color

            screen.blit(self.font.render(text, True, color), (menu_center_x+coordinate[0], menu_center_y+coordinate[1]))


    def update(self):
        current_tick = pygame.time.get_ticks()

        if current_tick - self.last_tick > self.select_cooldown:
            self.last_tick = current_tick
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.selected = 0
            if keys[pygame.K_DOWN]:
                self.selected = 1

    def run(self, fps=60):
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Jolly Jumpers - Main Menu')
        clock = pygame.time.Clock()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()
            self.draw(screen)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                run = False
                

            pygame.display.update()
            clock.tick(fps)
        
        #close window
        pygame.display.quit()
        return self.get_selection()

