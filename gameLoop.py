import driver
import traffic
import gameSetup
import pygame
from pygame.locals import *
import background
import mainMenuLoop

class GameLoop:
    def __init__(self):
        #Run the game window setup
        self.game = gameSetup.GameSetup()
        self.game.setup()

        #Initialize all needed objects
        self.gamedisplay = self.game.gamedisplay
        self.drivercar = driver.Driver(500, 400)
        self.background = background.Background()
        self.mainmenu = mainMenuLoop.TitleScreen(self.gamedisplay)
        self.lane1 = traffic.Traffic(110)
        self.lane2 = traffic.Traffic(230)
        self.lane3 = traffic.Traffic(370)
        self.lane4 = traffic.Traffic(500)

        #Group the lane objects together
        self.lanegroup = pygame.sprite.Group(self.lane1, self.lane2, self.lane3, self.lane4)

    def loop(self):
        #After a key is held down for 20 milliseconds, enter a new event of that key every 10 milliseconds
        pygame.key.set_repeat(20, 10)
        pygame.key.get_repeat()

        quit = False
        slowcount = 0

        #Run the main menu loop and determine if the game should be fully quit
        self.mainmenu.menu_loop()
        fullquit = self.mainmenu.fullquit

        while not quit:
            #If the user chooses to fully quit from the main menu, quit the loop
            if fullquit == True:
                quit = True
                break

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

            if self.background.y < 0:
                self.background.scroll()
            else:
                self.background.reset()

            #Loops through the queue of events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                    break
                if event.type == pygame.KEYDOWN:
                    #Move the driver left if the left key is pressed
                    if event.key == pygame.K_LEFT:
                        self.drivercar.moveLeft()
                    #Move the driver right if the right key is pressed
                    if event.key == pygame.K_RIGHT:
                        self.drivercar.moveRight()
                    #Increase the speed if the up key is pressed
                    if event.key == pygame.K_UP:
                        self.background.speedup()
                        self.lane1.speedup()
                        self.lane2.speedup()
                        self.lane3.speedup()
                        self.lane4.speedup()
                    #Decrease the speed if the down key is pressed
                    if event.key == pygame.K_DOWN:
                        self.background.slowdown()
                        self.lane1.slowdown()
                        self.lane2.slowdown()
                        self.lane3.slowdown()
                        self.lane4.slowdown()

            #print(self.drivercar.rect)
            #print(self.lane1.rect)
            #print(self.lane2.rect)
            #print(self.lane3.rect)
            #print(self.lane4.rect)

            #Loop through the lane group and see if the driver has collided with any lane object
            for lane in self.lanegroup:
                if pygame.sprite.collide_rect(self.drivercar, lane) == True:
                    quit = True
                    break

            #If the drivercar collides with the left or right wall of the background, quit the loop
            if self.drivercar.x <= 70 or self.drivercar.x >= 580:
                quit = True
                break

            #If the lowest speed for the lane objects is the lowest possible, start a count
            if self.lane1.speeds[0] <= 0.5:
                slowcount += 1
            else: slowcount = 0

            #If the slow count reaches 750 frames, quit the loop
            if slowcount == 750:
                quit = True
                break

            #Update the surface
            self.gamedisplay.blit(self.background.image, (self.background.x, self.background.y))

            #Update the models
            self.gamedisplay.blit(self.drivercar.image, (self.drivercar.x, self.drivercar.y))
            self.gamedisplay.blit(self.lane1.image, (self.lane1.x, int(self.lane1.y)))
            self.gamedisplay.blit(self.lane2.image, (self.lane2.x, int(self.lane2.y)))
            self.gamedisplay.blit(self.lane3.image, (self.lane3.x, int(self.lane3.y)))
            self.gamedisplay.blit(self.lane4.image, (self.lane4.x, int(self.lane4.y)))


            #Display the updated view
            pygame.display.flip()

        pygame.quit()
