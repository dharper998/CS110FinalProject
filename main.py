import pygame
from pygame.locals import *
import time
import random
import gameSetup
import gameLoop
import driver
import traffic

def main():
    #Creates game object and runs setup method
    game = gameSetup.GameSetup()
    game.setup()

    #Creates seperate variable for display and creates drivercar object
    gamedisplay = game.gamedisplay
    drivercar = driver.Driver(500, 300)
    lane1 = traffic.Traffic(100)
    lane2 = traffic.Traffic(200)
    lane3 = traffic.Traffic(700)
    lane4 = traffic.Traffic(800)

    #Creates a loop object and runs the loop method
    gameloop = gameLoop.GameLoop(gamedisplay, drivercar, lane1, lane2, lane3, lane4)
    gameloop.loop()
main()
