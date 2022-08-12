import pygame, sys, random
from pygame.math import Vector2

class Food:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1) # -1 ensures food always on-screen
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y) # creating 2D vector to determine position

    def draw_food(self):
        food_rect = pygame.Rect(int(self.pos.x) * cell_size, int(self.pos.y) * cell_size, cell_size, cell_size) # creates a rectangle: (xpos, ypos, h, w)
        pygame.draw.rect(screen, (66, 161, 255), food_rect)

pygame.init() # initialising pygame modules
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) # creating base surface (like a blank canvas)
clock = pygame.time.Clock() # limits how fast while loop can run

food = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # opposite of pygame.init()
            sys.exit() # ensures all parts of prog have stopped running

    screen.fill((230, 242, 233)) 
    food.draw_food()
    pygame.display.update() # ensures elements show up on screen
    clock.tick(60) # sets framerate: how many times the while loop can run per sec