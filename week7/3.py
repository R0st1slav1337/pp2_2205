import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 500
screen_height = 500

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Ball properties
ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed = 20

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            # Check if the ball is within the screen boundaries
            if event.key == pygame.K_UP and ball_y - ball_radius - ball_speed >= 0: 
                ball_y -= ball_speed # Move the ball up
            elif event.key == pygame.K_DOWN and ball_y + ball_radius + ball_speed <= screen_height: 
                ball_y += ball_speed # Move the ball down
            elif event.key == pygame.K_LEFT and ball_x - ball_radius - ball_speed >= 0:
                ball_x -= ball_speed # Move the ball left
            elif event.key == pygame.K_RIGHT and ball_x + ball_radius + ball_speed <= screen_width: 
                ball_x += ball_speed # Move the ball right

    # Fill the background
    screen.fill(white)

    # Draw the ball
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()