# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing 
pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60) # Create a font for displaying the game over message
font_small = pygame.font.SysFont("Verdana", 20) # Create a small font for displaying the score
game_over = font.render("Game Over", True, BLACK) # Display the game over message

background = pygame.image.load("week8/racer/AnimatedStreet.png") # Load the background image

# Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600)) # Set the display size
DISPLAYSURF.fill(WHITE) # Fill the display with white color
pygame.display.set_caption("Game") # Set the window name

# Load and play background music
pygame.mixer.music.load('week8/racer/background.wav') # Load the background music
pygame.mixer.music.play(-1)  # Play the music in a loop

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("week8/racer/Enemy.png") # Load the enemy image
        self.rect = self.image.get_rect() # Get the dimensions of the enemy image
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) # Set the initial position of the enemy

      def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) # Move the enemy down
        if (self.rect.top > 600): # Check if the enemy has moved off the screen
            SCORE += 1 # Increment the SCORE
            self.rect.top = 0 # Move the enemy to the top of the screen
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) # Move the enemy to a new location


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("week8/racer/Player.png") # Load the player image
        self.rect = self.image.get_rect() # Get the dimensions of the player image
        self.rect.center = (160, 520) # Set the initial position of the player
       
    def move(self):
        pressed_keys = pygame.key.get_pressed() # Get the keys pressed by the user
        if self.rect.top > 0: # Check if the player is within the top boundary
            if pressed_keys[K_UP]: 
                self.rect.move_ip(0, -5) # Move the player up
        if self.rect.bottom < SCREEN_HEIGHT: # Check if the player is within the bottom boundary
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5) # Move the player down
        
        if self.rect.left > 0: # Check if the player is within the left boundary
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0) # Move the player to the left
        if self.rect.right < SCREEN_WIDTH: # Check if the player is within the right boundary       
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0) # Move the player to the right

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("week8/racer/Coin.png") # Load the coin image
        self.image = pygame.transform.scale(self.image, (30, 30))  # Resize the coin image
        self.rect = self.image.get_rect() # Get the dimensions of the coin image
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) # Set the initial position of the coin
        self.value = random.randint(1, 3)  # Assign a random value (1 to 3)

    def move(self):
        self.rect.move_ip(0, SPEED)  # Move the coin down
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()  # Respawn the coin if it moves off the screen

    def respawn(self):
        self.rect.top = 0  # Move the coin to the top of the screen
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Move the coin to a new location
        self.value = random.randint(1, 3)  # Assign a new random value (1 to 3)

# Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1) # Add the enemy to the group
coins = pygame.sprite.Group()
coins.add(C1) # Add the coin to the group
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1 # Event is triggered every 1000ms
pygame.time.set_timer(INC_SPEED, 1000) # Set the timer for the event

# Game Loop
while True:
      
    # Cycles through all events occurring  
    for event in pygame.event.get(): 
        if event.type == INC_SPEED:  
              SPEED += 0.05 # Increase the speed of the game
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0)) # Draw the background image
    scores = font_small.render(str(SCORE), True, BLACK) 
    coins_collected_text = font_small.render("Coins: " + str(COINS_COLLECTED), True, BLACK) 
    DISPLAYSURF.blit(scores, (10,10)) # Display the score
    DISPLAYSURF.blit(coins_collected_text, (SCREEN_WIDTH - 100, 10)) # Display the number of coins collected

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect) # Draw the entity to the screen
        entity.move() # Move the entity

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.music.stop()  # Stop the background music
          pygame.mixer.Sound('week8/racer/crash.wav').play() # Play the crash sound
          time.sleep(0.5) # Pause the game for a short while
                   
          DISPLAYSURF.fill(RED) # Change the background color to red
          DISPLAYSURF.blit(game_over, (30,250)) # Display the game over message
          
          pygame.display.update() # Update the display
          for entity in all_sprites:
                entity.kill()  # Remove all sprites from the game
          time.sleep(2) # Pause the game for a short while
          pygame.quit() 
          sys.exit() # Exit the game

   # Check for collision with coins
    if pygame.sprite.spritecollideany(P1, coins):
        for coin in coins:
            if pygame.sprite.collide_rect(P1, coin):  # Check which coin was collected
                COINS_COLLECTED += coin.value  # Add the coin's value to the total
                coin.respawn()  # Respawn the coin

                # Increase speed every 15 coins collected
                if COINS_COLLECTED % 15 == 0:
                    SPEED += 0.3  # Increase the speed significantly

    pygame.display.update()
    FramePerSec.tick(FPS)