import random
import pygame
from pygame.locals import *

class Traffic(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)

        #initializes a traffic sprite off the top of the screen at the given x value for its lane
        self.y = random.randrange(-2000, -500)
        self.x = x

        #Chooses a random speed from 6 through 10 for the traffic object
        self.speeds = [1.0, 2.0, 3.0]
        self.randomspeed = random.choice(self.speeds)

        #Chooses a random image for the traffic objects appearance
        self.trafficimage1 = pygame.image.load('assets/' + "Black_viper.png").convert_alpha()
        self.trafficimage2 = pygame.image.load('assets/' + "Mini_van.png").convert_alpha()
        self.trafficimage3 = pygame.image.load('assets/' + "Mini_truck.png").convert_alpha()
        self.trafficimage4 = pygame.image.load('assets/' + "truck.png").convert_alpha()
        self.imagelist = [self.trafficimage1, self.trafficimage2, self.trafficimage3, self.trafficimage4]
        self.image = random.choice(self.imagelist)

        #Gets the appropriate rectangle for the object based on the chosen image
        self.rect = self.image.get_rect(left = self.x, top = self.y)

    def drive(self):
        #Increases the object y value by the current speed, moving it toward the bottom of the screen
        self.y += float(self.randomspeed)
        print(self.x, self.y)
        self.rect.move_ip(0, float(self.randomspeed))

    def reset(self):
        #Moves the object back to the origin position off the top of the screen and gives it a new random speed and image
        self.y = random.randrange(-2000, -500)
        self.randomspeed = random.choice(self.speeds)
        self.image = random.choice(self.imagelist)
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

    def speedup(self):
        if self.speeds[-1] < 5.0:
            self.speeds = [i + 0.10 for i in self.speeds]
            self.randomspeed += 0.10
        print(self.speeds)

    def slowdown(self):
        if self.speeds[0] > 0.5:
            self.speeds = [i - 0.10 for i in self.speeds]
            self.randomspeed -= 0.10
        print(self.speeds)
