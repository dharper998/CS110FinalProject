import pygame
from pygame.locals import *
import time
import random
import gameSetup
import gameLoop
import driver
#import traffic

def main():
    game = gameSetup.GameSetup()
    game.setup()
    gamedisplay = game.gamedisplay
    drivercar = driver.Driver(200, 200)
    loop = gameLoop.GameLoop(gamedisplay, drivercar)
    loop.loop()
main()
