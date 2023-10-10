'''
CS 150 Introduction to OOP

Demos a bouncing box
'''

import pygame
import random

# Specify the width and height of the screen for the game
SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 600

# Frames-Per-Second for game updates
FPS = 60

class Box():
    def __init__(self):
        self.rect = pygame.Rect(0, 200, 250, 250)
        self.velocity = [180,180]
        
    def update(self,dt):
        self.rect.x += self.velocity[0]*dt
        self.rect.y += self.velocity[1]*dt
        
        # Use the relevant attributes to check if rectangle has hit the edges
        # of the screen (0,0 is the upper left corner)
        random_multiplier = ((random.uniform(0.5,1.5)))
        if (self.rect.left < 0 or self.rect.right > SCREEN_WIDTH):
            self.velocity[0] *= (-1 * random_multiplier)
        if (self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT):
            self.velocity[1] *= (-1 * random_multiplier)

def play_game():
    # Initialize pygame
    pygame.init()
    pygame.font.init()

    # Initialize the screen
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )

    # Initialize game elements
    box = Box()

    # Initialize some game variables
    time = 0
    delta_t = 1/FPS

    # Setup the font and clock
    font  = pygame.font.SysFont('Arial',14)
    clock = pygame.time.Clock()

    # Main game loop
    while True:
        
        # Get the event corresponding to user input
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        # Draw the scene
        screen.fill((255,255,255)) # Fill the scene with white (specified by RGB tuple)

        box.update(delta_t) # Update the position of the box
        pygame.draw.rect(screen, (0,0,255), box.rect) # Draw a blue box at current position

        # Update and draw the current time in the bottom left corner
        time += delta_t
        text = font.render('Time=' + str(round(time,1)) + ' seconds',True,(0,0,0))
        screen.blit(text,(10,0.95*SCREEN_HEIGHT))

        # Update the screen
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


