import pygame
class HowToPlay:
    def init(self,gamedisplay):
        self.gamedisplay = gamedisplay
        self.background = pygame.image.load("assets/howtoplay.png").convert_alpha()
    def htp_loop(self):
        self.quit = False
        while not self.quit:
            self.gamedisplay.blit(self.backgroun, (0,0))
            self.button("Back", 500, 600, 100, 100, (0, 175, 0), (0, 255, 0), "Back")
    def button(self, msg, x, y, width, height, ic, ac, buttontype):
        #Get the position and state of the mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Initialize fonts, text surface, and text rectangle
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textSurf = smalltext.render(msg, True, (0, 0, 0))
        textRect = textSurf.get_rect()
        textRect.center = ((x + (width / 2)), (y + (height / 2)))
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.gamedisplay, ac, (x, y, width, height))
            self.gamedisplay.blit(textSurf, textRect)

        #If the mouse is clicked, check which button is pressed and perform the appropriate action
            if click[0] == 1 and buttontype == "Back":
                self.quit = True

        else:
            pygame.draw.rect(self.gamedisplay, ic, (x, y, width, height))
            self.gamedisplay.blit(textSurf, textRect)                 