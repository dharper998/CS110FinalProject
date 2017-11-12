
class Driver:
    def __init__(self, x, y, carimage):
        self.x = x
        self.y = y
        self.carimage = carimage

    def setupCar(self):
        gameDisplay.blit(self.carimage, (self.x, self.y))

    def moveLeft(self, K_LEFT):
        self.x -= 1
        return self.x

    def moveRight(self,K_RIGHT):
        self.x += 1
        return self.x
    def moveUp(self, K_UP):
	    self.y +=1
<<<<<<< HEAD
        return self.y
    def moveDown(self,K_DOWN):
	    self.y-=1
	    return self.y
=======
	    return self.y
    def moveDown(self,K_DOWN):
	    self.y-=1
	    return self.y
    def testing
>>>>>>> 4658894ce5057cb9046a8329ea17eaf166c5289f
