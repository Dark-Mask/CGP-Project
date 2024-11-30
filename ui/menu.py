import pygame
from assets import loader

class Menu:

    #constructor
    def __init__(self):
        self.menu = pygame.transform.scale(loader.get_menu(), (450, 500))
        self.menu_background = pygame.transform.scale(loader.menu_background(), (800, 600))
        self.options = [('Start', (170, 320)), ('Quit', (180, 420))]
        self.font = pygame.font.Font(None, 70)
        self.color1= pygame.color.Color(255, 63, 141)
        self.color2 = pygame.color.Color(240, 240, 240)
        self.selected = 0

    def change_option(self):
        #change selection
        if self.selected == 0:
            self.selected = 1
        else:
            self.selected = 0

    def get_selection(self):
        #start game
        return self.selected

    def draw(self, screen):
        #menu background
        cordX = (screen.get_width() - self.menu.get_width()) // 2
        cordY = (screen.get_height() - self.menu.get_height()) // 2
        screen.blit(self.menu_background, (0, 0))
        screen.blit(self.menu, (cordX, cordY))

        #draw options
        for i in range(len(self.options)):
            option = self.options[i]
            text, coord = option

            #highligh selection
            text = self.font.render(text, True, self.color1 if i == self.selected else self.color2)
            screen.blit(text, (cordX+coord[0], cordY+coord[1]))


