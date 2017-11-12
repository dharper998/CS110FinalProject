import pygame
from pygame.locals import *
import time
import random
import gameSetup
import gameLoop
import driver
#import traffic

def main():
    #create game object and run setup method
    game = gameSetup.GameSetup()
    game.setup()

    #create seperate variables for gamedisplay and drivercar to use as parameters
    gamedisplay = game.gamedisplay
    drivercar = driver.Driver(200, 200)

    #create loop object and run loop method
    loop = gameLoop.GameLoop(gamedisplay, drivercar)
    loop.loop()
main()
