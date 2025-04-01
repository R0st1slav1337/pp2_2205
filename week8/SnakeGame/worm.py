import pygame
from game_objects import GameObject, Point

class Worm(GameObject):
    def __init__(self, tile_width):
        # Initialize the worm with a starting position, color, and tile width
        super().__init__([Point(20, 20)], (0, 212, 130), tile_width) 
        self.DX = 1 # Initial direction of the worm (right)
        self.DY = 0 # Initial vertical direction of the worm

    def move(self):
        # Move the worm by updating the position of each point
        for i in range(len(self.points) - 1, 0, -1):
            self.points[i].X = self.points[i - 1].X
            self.points[i].Y = self.points[i - 1].Y

        # Update the head of the worm based on the current direction
        self.points[0].X += self.DX * self.tile_width
        self.points[0].Y += self.DY * self.tile_width

        # Wrap around the screen if the worm goes out of bounds
        if self.points[0].X >= 400:  # Right boundary
            self.points[0].X = 0
        elif self.points[0].X < 0:  # Left boundary
            self.points[0].X = 400 - self.tile_width

        # Wrap around the screen vertically
        if self.points[0].Y >= 300:  # Bottom boundary
            self.points[0].Y = 0
        elif self.points[0].Y < 0:  # Top boundary
            self.points[0].Y = 300 - self.tile_width

    # Increase the size of the worm by adding a new point at the current head position
    def increase(self, pos):
        self.points.append(Point(pos.X, pos.Y))
    
    # Process input events to change the direction of the worm
    def process_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                # Change direction to up
                self.DX = 0
                self.DY = -1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                # Change direction to down
                self.DX = 0
                self.DY = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                # Change direction to left
                self.DX = -1
                self.DY = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                # Change direction to right
                self.DX = 1
                self.DY = 0