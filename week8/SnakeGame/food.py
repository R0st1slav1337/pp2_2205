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

        # Initialize food properties for pause functionality
        self.paused_time = 0
        self.pause_start_time = None

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
        max_attempts = 100  # Ограничение на количество попыток найти свободное место
        for _ in range(max_attempts):
            # Generate a random position
            x = random.randint(0, (screen_width // self.tile_width) - 1) * self.tile_width
            y = random.randint(0, (screen_height // self.tile_width) - 1) * self.tile_width
            new_point = Point(x, y)

            # Ensure the position is not on the worm or walls
            if all(new_point != point for point in worm_points) and \
               all(new_point != point for point in wall_points):
                self.points = [new_point]  # Update the food position
                self.color = random.choice(list(self.colors.keys()))  # Assign a random color
                self.spawn_time = time.time()  # Reset the spawn time
                # Decide if the food will disappear again
                self.disappearing = random.choice([True, False])
                
                # Reset the pause properties
                self.paused_time = 0
                self.pause_start_time = None
                return

        # Если не удалось найти свободное место
        print("Warning: Could not find a free position for food.")

    def get_score(self):
        return self.colors[self.color]  # Return the score value based on the color
    
    def should_disappear(self):
        if not self.disappearing:
            return False
        effective_time = time.time() - self.spawn_time - self.paused_time
        return effective_time > 3
    
    # Pause the food timer
    def pause(self):
        if self.pause_start_time is None:
            self.pause_start_time = time.time()

    # Resume the food timer
    def resume(self):
        if self.pause_start_time is not None:
            self.paused_time += time.time() - self.pause_start_time
            self.pause_start_time = None