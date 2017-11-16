import pygame
from pygame.locals import *
import time
import random
import gameSetup
import gameLoop
import driver
import traffic

def main():
    #Creates a loop object and runs the loop method
    gameloop = gameLoop.GameLoop()
    gameloop.loop()
main()
