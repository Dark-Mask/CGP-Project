import pygame
import sys

def exit_event():
    #handle exit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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

def selection_event():
    #handle selection event
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                print('UP SELECTION')
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                print('DOWN SELECTION')
