import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Window size
width, height = 800, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Clock')

# Load images and resize them
clock_face = pygame.image.load('week7/clockbody.png')
clock_face = pygame.transform.scale(clock_face, (width, height))

minute_hand = pygame.image.load('week7/minutearrow.png')
minute_hand = pygame.transform.scale(minute_hand, (int(width * 0.5), int(height * 0.5)))

second_hand = pygame.image.load('week7/secondsarrow.png')
second_hand = pygame.transform.scale(second_hand, (int(width * 0.5), int(height * 0.5)))

# Center of the clock
center_x, center_y = width // 2, height // 2

# Fix FPS
clock = pygame.time.Clock()

# Function to rotate and display the hands
def rotate_and_blit(surface, image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, angle) # Rotate the image
    rect = rotated_image.get_rect(center=pivot) # Get the rect of the rotated image
    surface.blit(rotated_image, rect.topleft) # Blit the rotated image

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    # Correct the hand positions
    corrected_seconds = (seconds - 5) % 60 # Correct the second hand
    second_angle = -corrected_seconds * 6  

    corrected_minutes = (minutes - (5 // 60)) % 60 # Correct the minute hand
    minute_angle = -corrected_minutes * 6  

    # Clear the screen
    window.fill((255, 255, 255))
    window.blit(clock_face, (0, 0))

    # Display the hands
    rotate_and_blit(window, minute_hand, minute_angle, (center_x, center_y))
    rotate_and_blit(window, second_hand, second_angle, (center_x, center_y))

    pygame.display.flip()
    clock.tick(60)  # Limit FPS to 60