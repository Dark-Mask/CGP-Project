import pygame

class ObjectCollision:

    def __init__(self, bounce_factor, retension):
        self.bounce_factor = bounce_factor


    def check_collision(self, object1, object2):
        return object1.colliderect(object2)