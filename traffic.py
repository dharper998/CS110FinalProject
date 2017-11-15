import random

class Traffic(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.speeds = [1, 2, 3, 4, 5]
        self.images = ["Black_viper.png"]
        self.trafficimage = pygame.image.load("Black_viper.png")
        self.rect = self.trafficimage.get_rect()
