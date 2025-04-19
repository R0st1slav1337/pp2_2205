import pygame
from game_objects import GameObject, Point

class Wall(GameObject):
    def __init__(self, tile_width):
        # Initialize wall with an empty list of points and red color
        super().__init__([], (255, 0, 0), tile_width)
        self.level = 1 # Start at level 1
        self.max_level = 5  # Set the maximum number of levels
        self.load_level() # Load the initial level

    def load_level(self): # Load the wall level from a file
        f = open("week8/SnakeGame/levels/level{}.txt".format(self.level), "r")
        row = -1 # Initialize row counter
        col = -1 # Initialize column counter
        for line in f: # Read each line from the file
            row += 1
            col = -1
            for c in line: # Read each character in the line
                col += 1 
                if c == "#": # If the character is a wall block
                    # Add a point to the wall at the corresponding position
                    self.points.append(Point(col * self.tile_width, row * self.tile_width))
        f.close()

    def next_level(self): # Move to the next level
        self.level = (self.level + 1) % 5 # Cycle through levels 0, 1, 2, 3, 4
        if self.level > self.max_level:  # Loop back to level 1 after the last level
            self.level = 1
        self.points = [] # Clear the current wall points
        self.load_level() # Load the new level
