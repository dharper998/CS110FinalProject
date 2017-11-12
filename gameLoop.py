#import driver
#import traffic
import gameSetup
import pygame
from pygame.locals import *

class GameLoop:
    def __init__(self, gamedisplay, drivercar):
        self.gamedisplay = gamedisplay
        self.drivercar = drivercar
        
    def loop(self):
        while True:
            #checks incoming events like key presses
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break

            #sets background to white (will be replaced by road) and updates the screen to include the driver car
            self.gamedisplay.fill((255, 255, 255))
            self.gamedisplay.blit(self.drivercar.driverimg, (self.drivercar.x, self.drivercar.y))
            pygame.display.flip()
        pygame.quit()
