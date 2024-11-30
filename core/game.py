import pygame, sys
from core import settings
from ui import menu
from components import player
from pygame.locals import *

def start():
    #initialize pygame
    pygame.init()

    #screen configuration
    pygame.display.set_caption(settings.GAME_TITLE)
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HIGHT))

    #entity
    hero = player.Player(screen.get_width() / 2, screen.get_height() / 2, 50, 50, 'red')
    game_menu = menu.Menu()

    isGameStart = False
    isRunning = True
    #game loop
    while isRunning:
        screen.fill(settings.BACKGROUND_COLOR)

        #event handler
        events = pygame.event.get()

        #check window is close
        for event in events:
            if event.type == pygame.QUIT:
                isRunning = False

        if isGameStart:
            #handle movement event
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]: #move up
                hero.move(0, -5)
            if keys[pygame.K_s]: #move down
                hero.move(0, 5) 
            if keys[pygame.K_a]: #move left
                hero.move(-5, 0) 
            if keys[pygame.K_d]: #move right
                hero.move(5, 0) 

            #update character
            hero.draw(screen)

        else:
            #selecting game menu options
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        game_menu.change_option()
                    elif event.key == pygame.K_RETURN:
                        if game_menu.get_selection() == 0:
                            isGameStart = True
                        elif game_menu.get_selection() == 1:
                            isRunning = False
            #update menu
            game_menu.draw(screen)


        pygame.display.flip() #update screen
        pygame.time.Clock().tick(settings.FPS) #frame rate

    #terminate game
    pygame.quit()
    sys.exit()