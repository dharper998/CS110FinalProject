import pygame
from pygame.locals import *
import howto

class TitleScreen:
    def __init__(self, gamedisplay):
        self.gamedisplay = gamedisplay
        self.y = 300
        self.stevencarx = -1000
        self.colincarx = 1850
        self.stevenimage = pygame.image.load("assets/steven_police.png").convert_alpha()
        self.background = pygame.image.load("assets/Mainscreen.png").convert_alpha()
        self.howto = howto.HowToPlay(gamedisplay)
        self.title = pygame.image.load("assets/title.png").convert_alpha()
    def menu_loop(self):
        self.quit = False
        self.fullquit = False
        self.htp = False
        self.framecount = 0
        while not self.quit:

            #Loop through the queue of events and check if the quit button has been pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    self.fullquit = True

            #If the quit button is pressed, fully quit the game
            if self.fullquit == True:
                pygame.quit()
                break

            if self.htp == True:
                self.howto.htp_loop()
                self.htp = False

            #Update the background
            self.gamedisplay.blit(self.background, (0,0))
            
            #add title
            #myfont = pygame.font.SysFont("impact", 100)
            #label = myfont.render("Colin's Wild Ride", 1, (0,0,0))
            #self.gamedisplay.blit(label, (140, 80))
            self.gamedisplay.blit(self.title, (-25,0))
            #Update the models
            if self.stevencarx == 2000:
                self.stevencarx = -1000
            self.gamedisplay.blit(self.stevenimage, (self.stevencarx, self.y))
            for i in range(10):
                self.stevencarx += 1
                self.gamedisplay.blit(self.stevenimage, (self.stevencarx, self.y))


            #Update the buttons
            self.button("Start!", 100, 300, 100, 100, (0, 175, 0), (0, 255, 0), "Start")
            self.button("How To Play", 350, 300, 150, 100, (0, 0, 175), (0, 100, 255), "HTP")
            self.button("Quit", 650, 300, 100, 100, (175, 0, 0), (255, 0, 0), "Quit")


            #Display the updated view
            pygame.display.flip()

    def button(self, msg, x, y, width, height, ic, ac, buttontype):
        #Get the position and state of the mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Initialize fonts, text surface, and text rectangle
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textSurf = smalltext.render(msg, True, (0, 0, 0))
        textRect = textSurf.get_rect()
        textRect.center = ((x + (width / 2)), (y + (height / 2)))

        #If the mouse position is in the button, draw the active color on top
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.gamedisplay, ac, (x, y, width, height))
            self.gamedisplay.blit(textSurf, textRect)

            #If the mouse is clicked, check which button is pressed and perform the appropriate action
            if click[0] == 1 and buttontype == "Start":
                self.quit = True
            elif click[0] == 1 and buttontype == "HTP":
                self.htp = True
            elif click[0] == 1 and buttontype == "Quit":
                self.fullquit = True

        #If the mouse position is outside the button, draw the inactive color on top
        else:
            pygame.draw.rect(self.gamedisplay, ic, (x, y, width, height))
            self.gamedisplay.blit(textSurf, textRect)
