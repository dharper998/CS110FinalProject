import pygame
pygame.init()

white = (255, 255, 255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)

#Turns (display area) into a pixel array
pixAr = pygame.PixelArray(gameDisplay)

#single pixel at [x][y]
pixAr[10][20] = green

#(Where, color, two coordinates to connect with the line)
pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5)

#(Where, color, (top right x, top right y, width, height))
pygame.draw.rect(gameDisplay, red, (400,400,50,25))

#(Where, color, (center x, center y), radius)
pygame.draw.circle(gameDisplay, white, (150,150), 75)


#General button function
#msg = text on button
#x = the x location of the top left coordinate of the button box
#y = the y location of the top left coordinate of the button box
#w = button width
#h = button height
#ic = inactive color (when a mouse is not hovering)
#ac: active color (when a mouse is hovering)
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
