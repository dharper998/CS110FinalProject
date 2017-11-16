import driver
import traffic
import gameSetup
import pygame
from pygame.locals import *

class GameLoop:
    def __init__(self, gamedisplay, drivercar, lane1, lane2, lane3, lane4):
        self.gamedisplay = gamedisplay
        self.drivercar = drivercar
        self.lane1 = lane1
        self.lane2 = lane2
        self.lane3 = lane3
        self.lane4 = lane4
        self.lanegroup = pygame.sprite.Group(self.lane1, self.lane2, self.lane3, self.lane4)

    def loop(self):
        pygame.key.set_repeat(20, 10)
        pygame.key.get_repeat()
        quit = False
        while not quit:
            #For each lane object, if it is still on the screen it drives toward the bottom, otherwise it is reset
            if self.lane1.y < 900:
                self.lane1.drive()
            else:
                self.lane1.reset()

            if self.lane2.y < 900:
                self.lane2.drive()
            else:
                self.lane2.reset()

            if self.lane3.y < 900:
                self.lane3.drive()
            else:
                self.lane3.reset()

            if self.lane4.y < 900:
                self.lane4.drive()
            else:
                self.lane4.reset()

            #Loops through the queue of events
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

            #Checks if the driver has collided with any lane sprite
            ###### Doesn't work yet
            #for lane in self.lanegroup:
                #if pygame.sprite.collide_rect(self.drivercar, lane) == True:
                    #quit = True
                    #break
            ######

            #Update the surface
            self.gamedisplay.fill((255, 255, 255))

            #Update the models
            self.gamedisplay.blit(self.drivercar.driverimg, (self.drivercar.x, self.drivercar.y))
            self.gamedisplay.blit(self.lane1.randomimage, (self.lane1.x, self.lane1.y))
            self.gamedisplay.blit(self.lane2.randomimage, (self.lane2.x, self.lane2.y))
            self.gamedisplay.blit(self.lane3.randomimage, (self.lane3.x, self.lane3.y))
            self.gamedisplay.blit(self.lane4.randomimage, (self.lane4.x, self.lane4.y))


            #Display the updated view
            pygame.display.flip()

        pygame.quit()
