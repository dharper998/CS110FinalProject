import pygame
from pygame.locals import *

class GameSetup:
    def __init__(self):
        self.display_width = 1000
        self.display_height = 800
        self.gamedisplay = pygame.display.set_mode((self.display_width, self.display_height))
        self.clock = pygame.time.Clock()

    def setup(self):
        pygame.init()
        pygame.display.set_caption('Title')
        driver_width = 73
