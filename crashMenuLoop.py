
class CrashMenuLoop:
    def __init__(self, gamedisplay):
        self.gamedisplay = gamedisplay

    def crash_loop(self):
        self.quit = False
        self.fullquit = False
        while not self.quit:

            #Loop through the queue of events and check if the quit button has been pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    self.fullquit = True

            #If the window is closed
            if self.fullquit == True:
                pygame.quit()
                break

            #Update the background
            self.gamedisplay.fill((255, 255, 255))

            #Update the buttons
            self.button("Restart", 100, 100, 100, 100, (0, 175, 0), (0, 255, 0), "Restart")
            self.button("Quit", 500, 100, 100, 100, (175, 0, 0), (255, 0, 0), "Quit")

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
                if click[0] == 1 and buttontype == "Restart":
                    self.quit = True
                #elif click[0] == 1 and buttontype == "HTP":
                    #####ADD CALL TO HOW TO PLAY SCREEN HERE#####
                elif click[0] == 1 and buttontype == "Quit":
                    self.fullquit = True

                #If the mouse position is outside the button, draw the inactive color on top
            else:
                pygame.draw.rect(self.gamedisplay, ic, (x, y, width, height))
                self.gamedisplay.blit(textSurf, textRect)
