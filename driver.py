import pygame
from pygame.locals import *
import random

class Driver(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        #Creates the driver object at the given location and sets its appearance to the taxi image
        self.x = x
        self.y = y
        self.driverimg = pygame.image.load("taxi.png")
        self.rect = self.driverimg.get_rect()

    def moveLeft(self):
        #Decreases the driver object's x value by 10, moving it left
        self.x -= 10

    def moveRight(self):
        #Increases the driver object's x value by 10, moving it right
        self.x += 10
