import pygame

class Point:
    def __init__(self, X, Y):
        self.X = X # X coordinate of the point
        self.Y = Y # Y coordinate of the point

class GameObject:
    def __init__(self, points, color, tile_width):
        self.points = points # List of points representing the object
        self.color = color # Color of the object
        self.tile_width = tile_width # Width of each tile in the grid

    def draw(self, screen):
        for point in self.points: # Iterate through each point in the object
            # Draw a rectangle at the point's coordinates with the object's color
            pygame.draw.rect(screen, self.color, pygame.Rect(point.X, point.Y, self.tile_width, self.tile_width))
            # Draw a border around the rectangle
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(point.X, point.Y, self.tile_width, self.tile_width), 1) 