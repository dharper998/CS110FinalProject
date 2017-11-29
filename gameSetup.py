import pygame
from pygame.locals import *

class GameSetup:
    def __init__(self):
        self.display_width = 840
        self.display_height = 650
        self.gamedisplay = pygame.display.set_mode((self.display_width, self.display_height))
        self.clock = pygame.time.Clock()

    def setup(self):
        '''
        Initializes pygame and titles the window
        Paramlist: none
        Return: none
        '''
        pygame.init()
        pygame.display.set_caption("Colin's Wild Ride")
