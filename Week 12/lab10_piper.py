'''
A simple game where you play as a sandpiper trying to catch clams on a beach.
There is a oscillating wave which you will lose if you touch and an enemy crab
follows you around which will make you lose if it touches you. Good luck!

CS 150 Lab 10

Name: Finn Ellingwood

Creativity: I incorporated a crab enemy which follows the player around
and if it comes it contact with the player, the game is over. It moves
at one step every two seconds because the game was too hard when it moved
faster. I also made the beach sand colored and made the png files for
each entity transparent to look better on the sand.
'''
import pygame
import random
import math

# Constants to determine the size of the screen
SCREEN_WIDTH  = 500
SCREEN_HEIGHT = 500

# Number of clams to draw at the beginning of the game (or when regenerating)
NUM_CLAMS = 10

# Amount the player should move with each key press
STEP = 50

# Frames-per-second for the game
FPS = 60

# Speed of the crab: 1 is one step per second, 0.5 if one step every 2 seconds
CRAB_SPEED = 0.5

# Player image file variable
PIPER_PHOTO = 'piper.png'

# Clam image file variable
CLAM_PHOTO = 'clam.png'

# Crab image file variable
CRAB_PHOTO = 'crab.png'

class Entity():
    '''Base class for all game entities

    The game will create instances of the child classes of Entity

    Attributes:
        rect: A pygame.Rect that describes the location and size of the entity
    '''
    def __init__(self, x, y, width, height):
        '''Initialize an Entity

        Args:
            x, y: Initial x,y position for entity
            width: Width of entity's rectangle
            height: Height of entity's rectangle
        '''
        self.rect = pygame.Rect(x, y, width, height)
    
    def get_x(self):
        '''Return the current x-coordinate'''
        return self.rect.x
    
    def set_x(self, value):
        '''Set the x-coordinate to value'''
        self.rect.x = value
    
    def shift_x(self, shift):
        '''Shift the x-coordinate by shift (positively or negatively)'''
        self.rect.x += shift
    
    def get_y(self):
        '''Return the current y-coordinate'''
        return self.rect.y
    
    def set_y(self, value):
        '''Set the y-coordinate to value'''
        self.rect.y = value
    
    def shift_y(self, shift):
        '''Shift the y-coordinate by shift (positively or negatively)'''
        self.rect.y += shift
        
    def collide(self, collision):
        return pygame.sprite.collide_rect(self, collision)
    
class Player(Entity):
    def __init__(self):
        '''Initialize a Player (inherited from Entity)'''
        super().__init__(0, 0, 50, 50)
        img = pygame.image.load(PIPER_PHOTO)
        self.image = pygame.transform.scale(img, self.rect.size)
        
    def shift_x(self, shift):
        '''Shift the x-coordinate by shift (positively or negatively)'''
        self.rect.x += shift
    
    def shift_y(self, shift):
        '''Shift the y-coordinate by shift (positively or negatively)'''
        self.rect.y += shift
        
    def render(self, display):
        '''Renders the player entity to the screen given the display'''
        display.blit(self.image, self.rect)
        
class Clam(Entity):
    def __init__(self):
        '''Initialize a Clam (inherited from Entity)'''
        self.visible = True
        x = (random.randint(0.5*SCREEN_WIDTH, SCREEN_WIDTH-30))
        y = (random.randint(0, SCREEN_HEIGHT-30))
        super().__init__(x, y, 30, 30)
        img = pygame.image.load(CLAM_PHOTO)
        self.image = pygame.transform.scale(img, self.rect.size)
        
    def render(self, display):
        '''Renders the clam entity to the screen given the display'''
        if self.visible:
            display.blit(self.image, self.rect)
            
class Crab(Entity):
    def __init__(self):
        '''Initialize a Crab (inherited from Entity)'''
        super().__init__(SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.5, 50, 50)
        img = pygame.image.load(CRAB_PHOTO)
        self.image = pygame.transform.scale(img, self.rect.size)
        
    def shift_x(self, shift):
        '''Shift the x-coordinate by shift (positively or negatively)'''
        self.rect.x += shift
    
    def shift_y(self, shift):
        '''Shift the y-coordinate by shift (positively or negatively)'''
        self.rect.y += shift
        
    def render(self, display):
        '''Renders the crab entity to the screen given the display'''
        display.blit(self.image, self.rect)
        
class Wave(Entity):
    def __init__(self):
        '''Initialize the wave entity (inherited from Entity)'''
        width = 0.75*SCREEN_WIDTH
        super().__init__(width, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        
    def render(self, display):
        '''Renders the moving wave entity to the screen given the display'''
        color = pygame.Color(0,0,255)
        pygame.draw.rect(display, color, self.rect)
        
def play_game(max_time):
    '''Main game function for Piper's adventure

    Args:
        max_time: Number of seconds to play for
    '''
    
    # Initialize the pygame engine
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Arial',14)
    clock = pygame.time.Clock()

    # Sets up screen with proper size and gives it the caption of the name of the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Piper's adventures")

    # Initialize Player, Wave, Crab, and Clams
    player = Player()
    crab = Crab()
    clams = []
    for i in range(NUM_CLAMS):
        clams.append(Clam())
    wave = Wave()
    time  = 0
    score = 0
    counter = 0

    # Main game loop
    while time < max_time:

        # Obtain any user inputs
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
          break

        # Screen origin (0, 0) is the upper-left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.shift_x(STEP)
            elif event.key == pygame.K_LEFT:
                player.shift_x(-STEP)
            elif event.key == pygame.K_UP:
                player.shift_y(-STEP)
            elif event.key == pygame.K_DOWN:
                player.shift_y(STEP)
        
        # Determine if Piper gathered more clams
        for i in range(NUM_CLAMS):
            if Entity.collide(player, clams[i]) and time > 1 and clams[i].visible:
                clams[i].visible = False
                score += 1
                
        # Move crab enemy one tile towards the player per second
        if (counter % FPS == 0):
            if crab.rect.left < player.rect.left:
                crab.shift_x(STEP)
            if crab.rect.left > player.rect.left:
                crab.shift_x(-STEP)
            if crab.rect.top < player.rect.top:
                crab.shift_y(STEP)
            if crab.rect.top > player.rect.top:
                crab.shift_y(-STEP)
            
       
        # Update the position of the wave
        wave.set_x((0.75 * SCREEN_WIDTH) - (0.25 * SCREEN_WIDTH * math.sin(time)))
       
        # When the wave has reached its peak create new clams
        if wave.rect.left == 0.5 * SCREEN_WIDTH:
            clams = []
            for i in range(NUM_CLAMS):
                clams.append(Clam())
                clams[i].render(screen)
            

        # If the piper touched the wave the game is over...
        if wave.collide(player):
            time = max_time
            
        # If the piper touched the crab the game is over...
        if crab.collide(player):
            time = max_time

        # Draw all of the game elements
        screen.fill([245, 234, 132])
        
        # Draw clams
        for i in range(NUM_CLAMS):
            clams[i].render(screen)
        
        # Draw piper
        player.render(screen)
        
        # Draw crab
        crab.render(screen)
        
        # Draw wave
        wave.render(screen)
       
        # Render the current time and score
        text = font.render('Time = ' + str(round(max_time-time, 1)), True, (0, 0, 0))
        screen.blit(text, (10, 0.95*SCREEN_HEIGHT))
    
        text = font.render('Score = ' + str(score), True, (0, 0, 0))
        screen.blit(text, (10, 0.90*SCREEN_HEIGHT))

        # Render next frame
        pygame.display.update()
        clock.tick(FPS)

        # Update game time by advancing time for each frame
        time += 1.0/FPS
        counter += CRAB_SPEED

    # When game is lost or time is elapsed
    print('Game over!')
    print('Score =', score)

    pygame.display.quit()
    pygame.quit()

# Starts the game when program is run through the terminal
if __name__ == "__main__":
    play_game(30)
