class Background:
	def __init__(self, gamedisplay)
		self.Background1 = pygame.image.load('assets/'+'Scrolling_Background.png')
		self.x = 500
		self.y = 0
		self.speed = 5
	def Scroll(self):
		self.y += (int(self.speed))
		
