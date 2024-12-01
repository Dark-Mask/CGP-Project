import pygame

class ObjectGravity:

    def __init__(self, gravity):
        self.velocity = 0
        self.gravity = gravity

    def apply_gravity(self, object):
        #apply gravity
        self.velocity += self.gravity

        #update position
        object.move(0, self.velocity)