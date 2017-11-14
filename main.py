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

    #Creates seperate variable for disply and creates drivercar object
    gamedisplay = game.gamedisplay
    drivercar = driver.Driver(200, 200)

    #Creates a loop object and runs the loop method
    gameloop = gameLoop.GameLoop(gamedisplay, drivercar)
    gameloop.loop()
main()
