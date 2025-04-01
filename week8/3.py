import pygame
import sys

# Base scene class
class SceneBase:
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        raise NotImplementedError # Check if the method is implemented

    def Update(self):
        raise NotImplementedError 

    def Render(self, screen):
        raise NotImplementedError

    def SwitchToScene(self, next_scene):
        self.next = next_scene # Switch to the next scene

    def Terminate(self):
        self.SwitchToScene(None) # Terminate the scene

# Function to run the game
def run_game(width, height, fps, starting_scene):
    pygame.init() # Initialize Pygame
    pygame.font.init() # Initialize the font
    screen = pygame.display.set_mode((width, height)) # Set the screen size
    pygame.display.set_caption("Paint Application") # Set the window title
    clock = pygame.time.Clock() # Create a clock object

    active_scene = starting_scene # Set the starting scene

    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed() # Get the pressed keys

        # Filter events
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT: # Check if the user wants to quit
                quit_attempt = True # Set the quit attempt to True
            elif event.type == pygame.KEYDOWN: # Check if a key is pressed
                alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT] # Check if the Alt key is pressed
                if event.key == pygame.K_ESCAPE: # Check if the Escape key is pressed
                    quit_attempt = True # Set the quit attempt to True
                elif event.key == pygame.K_F4 and alt_pressed: # Check if the Alt + F4 keys are pressed
                    quit_attempt = True # Set the quit attempt to True

            if quit_attempt: # Check if the user wants to quit
                active_scene.Terminate() # Terminate the scene
            else:
                filtered_events.append(event) # Append the event to the filtered events

        active_scene.ProcessInput(filtered_events, pressed_keys) # Process the input
        active_scene.Update() # Update the scene
        active_scene.Render(screen) # Render the scene

        active_scene = active_scene.next # Switch to the next scene

        pygame.display.flip() # Update the display
        clock.tick(fps) # Set the frame rate

# Title scene
class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self) # Initialize the base scene
        self.options = ["Start painting", "Exit game"] # Set the options
        self.selected_option = 0 # Set the selected option
        self.font = pygame.font.Font(None, 40) # Set the font

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN: # Check if a key is pressed
                if event.key == pygame.K_RETURN: # Check if the Enter key is pressed
                    if self.selected_option == 0: # Check if the selected option is "Start painting"
                        self.SwitchToScene(DrawingScene()) # Switch to the drawing scene
                    elif self.selected_option == 1: # Check if the selected option is "Exit game"
                        self.Terminate() # Terminate the game
                elif event.key == pygame.K_UP: # Change the selected option
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN: # Change the selected option
                    self.selected_option = (self.selected_option + 1) % len(self.options) 

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0)) # Fill the screen with black color
        for i, option in enumerate(self.options): # Iterate through the options
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255) # Change the color of the selected option
            text = self.font.render(option, True, color) # Render the text
            screen.blit(text, (100, 100 + i * 60)) # Draw the text

# Drawing scene
class DrawingScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.screen_color = (255, 255, 255)  # Set the screen color
        self.colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0), (128, 0, 128)]  # Set the colors
        self.brush_color = self.colors[0]  # Set the brush color
        self.brush_size = 5  # Set the brush size
        self.drawing = False  # Check if the user is drawing
        self.last_pos = None  # Last position of the mouse
        self.needs_clear = True
        self.mode = 'brush'  # 'brush', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus', 'eraser'
        self.start_pos = None  # Start position of the shape
        print("\nDrawing Instructions:\n"
              "- LMB: Draw\n- RMB: Change brush color\n"
              "- Scroll Up: Increase brush size\n"
              "- Scroll Down: Decrease brush size\n"
              "- C: Clear the canvas\n"
              "- S: Save the drawing\n"
              "- 1: Circle mode\n"
              "- 2: Square mode\n"
              "- 3: Right triangle mode\n"
              "- 4: Equilateral triangle mode\n"
              "- 5: Rhombus mode\n"
              "- B: Brush mode\n"
              "- E: Eraser mode")  # Print the instructions

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:  # Check if the mouse button is pressed
                if event.button == 1:
                    if self.mode in ['circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        self.start_pos = event.pos  # Set the start position of the shape
                    else:
                        self.drawing = True  # Start drawing
                        self.last_pos = event.pos  # Set the last position
                elif event.button == 3:
                    self.change_brush_color()  # Change the brush color
                elif event.button == 4:
                    self.brush_size = min(50, self.brush_size + 1)  # Increase the brush size
                elif event.button == 5:
                    self.brush_size = max(1, self.brush_size - 1)  # Decrease the brush size
            elif event.type == pygame.MOUSEBUTTONUP:  # Check if the mouse button is released
                if self.start_pos and self.mode in ['circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                    self.draw_shape(event.pos)  # Draw the shape
                    self.start_pos = None  # Reset the start position
                self.drawing = False  # Stop drawing
            elif event.type == pygame.MOUSEMOTION and self.drawing and self.last_pos is not None:  # Check if the mouse is moving
                color = (255, 255, 255) if self.mode == 'eraser' else self.brush_color  # Change the color to white if eraser mode is enabled
                pygame.draw.line(screen, color, self.last_pos, event.pos, self.brush_size)  # Draw a line
                self.last_pos = event.pos  # Update the last position
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.needs_clear = True  # Clear the canvas
                elif event.key == pygame.K_s:
                    self.save_drawing()  # Save the drawing
                elif event.key == pygame.K_1:
                    self.mode = 'circle'  # Change the mode to circle
                elif event.key == pygame.K_2:
                    self.mode = 'square'  # Change the mode to square
                elif event.key == pygame.K_3:
                    self.mode = 'right_triangle'  # Change the mode to right triangle
                elif event.key == pygame.K_4:
                    self.mode = 'equilateral_triangle'  # Change the mode to equilateral triangle
                elif event.key == pygame.K_5:
                    self.mode = 'rhombus'  # Change the mode to rhombus
                elif event.key == pygame.K_b:
                    self.mode = 'brush'  # Change the mode to brush
                elif event.key == pygame.K_e:
                    self.mode = 'eraser'  # Change the mode to eraser

    def Update(self):
        pass

    def Render(self, screen):
        if self.needs_clear:
            screen.fill(self.screen_color)  # Clear the screen
            self.needs_clear = False  # Reset the flag

    def draw_shape(self, end_pos):
        x1, y1 = self.start_pos  # Get the start position of the shape
        x2, y2 = end_pos  # Get the end position of the shape
        width, height = abs(x2 - x1), abs(y2 - y1)  # Get the width and height of the shape
        rect = pygame.Rect(min(x1, x2), min(y1, y2), width, height)  # Create a rectangle

        if self.mode == 'circle':
            radius = max(width, height) // 2  # Get the radius of the circle
            center = (rect.left + rect.width // 2, rect.top + rect.height // 2)  # Get the center of the circle
            pygame.draw.circle(screen, self.brush_color, center, radius)  # Draw the circle
        elif self.mode == 'square':
            side = min(width, height)  # Make the square's sides equal
            pygame.draw.rect(screen, self.brush_color, pygame.Rect(x1, y1, side, side))  # Draw the square
        elif self.mode == 'right_triangle':
            points = [(x1, y1), (x1, y2), (x2, y2)]  # Define the vertices of the right triangle
            pygame.draw.polygon(screen, self.brush_color, points)  # Draw the right triangle
        elif self.mode == 'equilateral_triangle':
            side = min(width, height)  # Use the smaller dimension for the triangle's side
            points = [(x1 + side // 2, y1), (x1, y1 + side), (x1 + side, y1 + side)]  # Define the vertices
            pygame.draw.polygon(screen, self.brush_color, points)  # Draw the equilateral triangle
        elif self.mode == 'rhombus':
            points = [(x1 + width // 2, y1), (x1, y1 + height // 2), (x1 + width // 2, y2), (x2, y1 + height // 2)]  # Define the vertices
            pygame.draw.polygon(screen, self.brush_color, points)  # Draw the rhombus

    def change_brush_color(self):
        current_index = self.colors.index(self.brush_color)  # Get the current index of the brush color
        self.brush_color = self.colors[(current_index + 1) % len(self.colors)]  # Change the brush color

    def save_drawing(self):
        pygame.image.save(screen, "drawing.png")  # Save the drawing
        print("Drawing is saved as drawing.png")

# Start the program
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # Set the screen size
    run_game(800, 600, 60, TitleScene()) # Run the game
    pygame.quit()
    sys.exit()