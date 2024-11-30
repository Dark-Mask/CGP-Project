import pygame
import sys

def exit_event(events):
    #handle exit event
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def select_menu(events, menu, game):
    #handle selection event
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menu.change_option()
            elif event.key == pygame.K_DOWN:
                menu.change_option()
            elif event.key == pygame.K_RETURN:
                if menu.get_selection() == 0:
                    game.isGameStart = True
                elif menu.get_selection() == 1:
                    game.isRunning = False

def movement_event(entity):
    #handle movement event
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]: #move up
        entity.move(0, -5)

    if keys[pygame.K_s]: #move down
        entity.move(0, 5) 

    if keys[pygame.K_a]: #move left
        entity.move(-5, 0) 
        
    if keys[pygame.K_d]: #move right
        entity.move(5, 0) 
