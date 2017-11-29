import pygame
from pygame.locals import *

class CrashMenuLoop:

    def __init__(self, gamedisplay):
        self.gamedisplay = gamedisplay

    def crash_loop(self, dodged):
        '''
        Displays the crash menu
        Paramlist: dodged (variable tracking how many cars the user has successfully dodged)
        Return: none
        '''

        self.restart = True
        self.quit = False
        self.fullquit = False
        self.dodged = dodged

        #Create the text font
        myfont = pygame.font.SysFont("monospace", 38)

        #Crash mp3 plays
        pygame.mixer.music.load('assets/crash_sound.mp3')
        pygame.mixer.music.play(0)

        #If quit is true, return to the main menu. If fullquit is true, quit the game
        while not self.quit:

            #Loop through the queue of events and check if the quit button has been pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    self.fullquit = True

            #If the window is closed, quit the game
            if self.fullquit == True:
                pygame.quit()
                break

            #Draw a background rectangle for the score text, adjust width based on size of score
            if self.dodged < 10:
                pygame.draw.rect(self.gamedisplay, (0, 0, 0), (200, 10, 440, 85))
            else: pygame.draw.rect(self.gamedisplay, (0, 0, 0), (200, 10, 460, 85))

            #Render score and label text
            label = myfont.render("YOU CRASHED", 1, (255,255,255))
            score = myfont.render("You Dodged: " + str(self.dodged) + " Cars", 1, (255, 255, 255))
            self.gamedisplay.blit(label, (295, 15))
            self.gamedisplay.blit(score, (215, 50))

            #Update the buttons
            self.button("Restart", 235, 100, 100, 100, (0, 175, 0), (0, 255, 0), "Restart")
            self.button("Quit", 500, 100, 100, 100, (175, 0, 0), (255, 0, 0), "Quit")

            #Display the updated view
            pygame.display.flip()

    def button(self, msg, x, y, width, height, ic, ac, buttontype):
        '''
        Displays and handles interaction with a button on the screen
        Paramlist: msg (The text on the button), x (x position of the top left corner), y (y position of the top left corner), width (width of the button), height (height of the button), ic (inactive color), ac (active color), buttontype (determines what action takes place when the button is clicked)
        Return: none
        '''

        #Get the position and state of the mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Initialize fonts, text surface, and text rectangle
        buttontext = pygame.font.Font("freesansbold.ttf", 20)
        textSurf = buttontext.render(msg, True, (0, 0, 0))
        textRect = textSurf.get_rect()
        textRect.center = ((x + (width / 2)), (y + (height / 2)))

        #If the mouse position is in the button, draw the active color on top
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.gamedisplay, ac, (x, y, width, height))
            self.gamedisplay.blit(textSurf, textRect)

            #If the mouse is clicked, check which button is pressed and perform the appropriate action
            if click[0] == 1 and buttontype == "Restart":
                self.restart = True
                self.quit = True
            elif click[0] == 1 and buttontype == "Quit":
                self.restart = False
                self.quit = True
                self.fullquit = True

        #If the mouse position is outside the button, draw the inactive color on top
        else:
            pygame.draw.rect(self.gamedisplay, ic, (x, y, width, height))
            self.gamedisplay.blit(textSurf, textRect)
