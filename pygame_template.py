# Import needed modules
import pygame
import random
# set game constant variables
width = 360
height = 480
fps = 30
# you HAVE to run pygame.init to tell program to start pygame
pygame.init()
pygame.mixer.init()
# set the display size to our game constants and set to variable
screen = pygame.display.set_mode((width,height))
# set window title (name that opens on top bar of window)
pygame.display.set_caption("Pygame Template")
clock = pygame.time.Clock()
# set some color variables to use later (or just set background img variables)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# set bool to control game loop
gameOn = True

# start game loop
#     game loop will do 3 things
#     1. process input
#     2. update (sprite locations, or button inputs)
#     3. draw the screen with new information
while gameOn:
    # run loop at the correct speed
    clock.tick(fps)
    # add event listener, and set way to kill the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    # draw the screen
    screen.fill(black)
    # always put this LAST in the loop so that it draws 
    # the most up to date information from the loop
    pygame.display.flip()