import pygame, sys

pygame.init() # initialising pygame modules
screen = pygame.display.set_mode((400, 500)) # creating base surface (like a blank canvas)
clock = pygame.time.Clock() # limits how fast while loop can run

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            sys.exit() # ensures all parts of prog have stopped running

    screen.fill((230, 242, 233)) 
    pygame.display.update() # ensures elements show up on screen
    clock.tick(60) # sets framerate: how many times the while loop can run per sec