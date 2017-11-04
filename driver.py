
class Driver:
    def __init__(self, x, y, carimage):
        self.x = x
        self.y = y
        self.carimage = carimage

    def setupCar(self):
        gameDisplay.blit(self.carimage, (self.x, self.y))

    def moveLeft(self):
        self.x += 5
        return self.x

    def moveRight(self):
        self.x -= 5
        return self.x
