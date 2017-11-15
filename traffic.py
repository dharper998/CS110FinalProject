import random

class Traffic(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.speeds = [1, 2, 3, 4, 5]
        self.trafficimage1 = pygame.image.load("Black_viper.png")
        self.trafficimage2 = pygame.image.load("")
        self.trafficimage3 = pygame.image.load("")
        self.trafficimage4 = pygame.image.load("")
        self.imagelist = [self.trafficimage1, self.trafficimage2, self.trafficimage3, self.trafficimage4]
        self.randomimage = random.choice[imagelist]
        self.rect = self.trafficimage.get_rect()
