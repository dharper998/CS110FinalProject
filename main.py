import pygame
from pygame.locals import *
import time
import random
import gameSetup
import gameLoop
import driver
#import traffic

def main():
    #Creates game object and runs setup method
    game = gameSetup.GameSetup()
    game.setup()

    #Creates seperate variable for display and creates drivercar object
    gamedisplay = game.gamedisplay
    drivercar = driver.Driver(500, 300)

    #Creates a loop object and runs the loop method
    gameloop = gameLoop.GameLoop(gamedisplay, drivercar)
    gameloop.loop()
main()
