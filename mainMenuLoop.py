import pygame
class TitleScreen:
	def __init__(self, gamedisplay):
		self.gamedisplay = gamedisplay()
		self.StevenCarx = -50
		self.ColinCarx = 1850
		self.stcdevenimage = pygame.image.load("steven_police.png")
	def menu_loop(self):
		self.gamedisplay.bit(self.stevenimage,(StevenCarx, y))
		quit = False
		while not quit:
			for i in range(10):
				StevenCarx += 10
				self.gamedisplay.blit(self.stevenimage, (StevenCarx, y))

        #########
		while quit:
			break
        #########
	def button(msg,x,y,w,h,ic,ac):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
		else:
			pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

			smallText = pygame.font.Font("freesansbold.ttf",20)
			textSurf, textRect = text_objects(msg, smallText)
			textRect.center = ( (x+(w/2)), (y+(h/2)) )
			gameDisplay.blit(textSurf, textRect)
