import random

class Traffic(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speeds = [1, 2, 3, 4, 5]
        self.trafficimage1 = pygame.image.load("Black_viper.png")
        self.trafficimage2 = pygame.image.load("")
        self.trafficimage3 = pygame.image.load("")
        self.trafficimage4 = pygame.image.load("")
        self.imagelist = [self.trafficimage1, self.trafficimage2, self.trafficimage3, self.trafficimage4]
        self.randomimage = random.choice[imagelist]
        self.rect = self.trafficimage.get_rect()
    def setuploop(self):

    def lane1(self):


    def lane2(self):


    def lane3(self):


    def lan4(self):
