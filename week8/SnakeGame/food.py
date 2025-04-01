import pygame
import random
import time
from game_objects import GameObject, Point

class Food(GameObject):
    def __init__(self, tile_width):
        # Initialize food with a default position and color
        super().__init__([Point(120, 20)], (140, 205, 0), tile_width)
        self.colors = {
            (140, 205, 0): 1,  # Green: 1 point
            (255, 255, 0): 2,  # Yellow: 2 points
            (128, 0, 128): 3,  # Purple: 3 points
            (21, 36, 231): 4,  # Blue: 4 points
        }
        self.color = random.choice(list(self.colors.keys()))  # Random initial color
        self.spawn_time = time.time()  # Record the time when the food spawns
        # Randomly decide if the food will disappear
        self.disappearing = random.choice([True, False]) 

    # Check if the worm can eat the food
    def can_eat(self, head_location):
        result = None
        # Check if the food is at the same location as the worm's head
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break
        # Return the food point if it is eaten, otherwise return None
        return result
    
    # Spawn food at a random location on the screen
    def spawn(self, worm_points, wall_points, screen_width, screen_height):
        while True:
            # Generate a random position
            x = random.randint(0, (screen_width // self.tile_width) - 1) * self.tile_width
            y = random.randint(0, (screen_height // self.tile_width) - 1) * self.tile_width
            new_point = Point(x, y)

            # Ensure the position is not on the worm or walls
            if new_point not in worm_points and new_point not in wall_points:
                self.points = [new_point] # Update the food position
                self.color = random.choice(list(self.colors.keys()))  # Assign a random color
                self.spawn_time = time.time()  # Reset the spawn time
                # Decide if the food will disappear again
                self.disappearing = random.choice([True, False])
                break

    def get_score(self):
        return self.colors[self.color]  # Return the score value based on the color
    
    def should_disappear(self):
        # Check if the food is disappearing and has been on the screen for more than 3 seconds
        return self.disappearing and (time.time() - self.spawn_time > 3)