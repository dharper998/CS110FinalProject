import pygame

class GameSetup:
    def setup(self):
        pygame.init()
        display_width = 800
        display_height = 600
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Title')
        clock = pygame.time.Clock()
        driverimg = pygame.image.load('taxi.png')
        driver_width = 73
