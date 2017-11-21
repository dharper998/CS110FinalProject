import pygame
from pygame.locals import *
import random

class Driver(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        #Creates the driver object at the given location and sets its appearance to the taxi image
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/taxi.png').convert_alpha()
        self.rect = self.image.get_rect(left = (self.x + 63), top = (self.y + 14), width = 77, height = 180)

    def moveLeft(self):
        #Decreases the driver object's x value by 5, moving it left
        self.x -= 5
        self.rect.move_ip(-5, 0)

    def moveRight(self):
        #Increases the driver object's x value by 10, moving it right
        self.x += 5
        self.rect.move_ip(5, 0)
