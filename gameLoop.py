import driver
#import traffic
import gameSetup
import pygame
from pygame.locals import *

class GameLoop:
    def __init__(self, gamedisplay, drivercar):
        self.gamedisplay = gamedisplay
        self.drivercar = drivercar

    def loop(self):
        quit = False
        pygame.key.set_repeat(20, 10)
        pygame.key.get_repeat()
        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.drivercar.moveLeft()
                    if event.key == pygame.K_RIGHT:
                        self.drivercar.moveRight()
                    #if event.type == pygame.K_UP:

            #Update the surface
            self.gamedisplay.fill((255, 255, 255))

            #Update the models
            self.gamedisplay.blit(self.drivercar.driverimg, (self.drivercar.x, self.drivercar.y))

            #Display the updated view
            pygame.display.flip()

        pygame.quit()
