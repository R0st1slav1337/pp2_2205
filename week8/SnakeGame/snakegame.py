import pygame
from game_objects import GameObject
from worm import Worm
from wall import Wall
from food import Food
import psycopg2
from config import load_config

pygame.display.set_caption("Snake game")  # Set the window title

# Function to create a background pattern
def create_background(screen, width, height):
    colors = [(255, 255, 255), (212, 212, 212)]
    tile_width = 20
    y = 0
    while y < height:
        x = 0
        while x < width:
            row = y // tile_width
            col = x // tile_width
            # Draw the tile with alternating colors
            pygame.draw.rect(screen, colors[(row + col) % 2], pygame.Rect(x, y, tile_width, tile_width))
            x += tile_width
        y += tile_width

def get_or_create_user(username):
    """
    Check if the user exists in the database. If not, create a new user.
    """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Check if the user already exists
                cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
                user = cur.fetchone()

                if user:
                    print(f"Welcome back, {username}!")
                    return user[0]  # Return user_id
                else:
                    # Create a new user
                    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
                    user_id = cur.fetchone()[0]
                    conn.commit()
                    print(f"Hello, {username}! Your profile has been created.")
                    return user_id
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Database error: {error}")
        return None

def save_score(user_id, score, level):
    """
    Save the user's score in the database.
    """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                    (user_id, score, level)
                )
                conn.commit()
                print(f"Score of {score} at level {level} saved for user ID {user_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Database error: {error}")

# Main game logic
if __name__ == '__main__':
    # Prompt the user to enter their username
    username = input("Enter your username: ").strip()

    # Ensure the username is not empty
    while not username:
        print("Username cannot be empty. Please try again.")
        username = input("Enter your username: ").strip()

    # Get or create the user in the database
    user_id = get_or_create_user(username)

    if user_id:
        # Initialize pygame and create a window
        pygame.init()
        screen = pygame.display.set_mode((400, 300))
        clock = pygame.time.Clock()

        # Initialize game objects
        worm = Worm(20)
        food = Food(20)
        wall = Wall(20)

        # Initialize font for "Game Over" message
        font = pygame.font.Font(None, 50)
        small_font = pygame.font.Font(None, 30)

        # Initialize score and level counters
        score = 0
        level = 1
        speed = 5  # Initial game speed (frames per second)

        done = False
        paused = False

        # Main game loop
        while not done:
            filtered_events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check if the user wants to quit
                    done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_score(user_id, score, level)
                        food.pause()
                        print("Game paused. Progress saved.")
                    else:
                        food.resume()
                        print("Game resumed.")
                else:
                    filtered_events.append(event)

            if paused:
                pause_text = font.render("Paused", True, (255, 255, 0))
                screen.blit(pause_text, (130, 130))
                pygame.display.flip()
                clock.tick(5)
                continue

            worm.process_input(filtered_events)  # Process input for the worm
            worm.move()  # Move the worm

            # Check collision with walls
            for wall_point in wall.points:
                if worm.points[0].X == wall_point.X and worm.points[0].Y == wall_point.Y:
                    # Display "Game Over" message
                    text = font.render("Game Over!", True, (255, 0, 0))
                    screen.fill((0, 0, 0))  # Clear the screen
                    screen.blit(text, (100, 130))  # Draw the text at the center
                    pygame.display.flip()  # Update the display
                    pygame.time.delay(2000)  # Wait for 2 seconds
                    done = True
                    break

            # Check if the worm eats the food
            pos = food.can_eat(worm.points[0])
            if pos is not None:
                worm.increase(pos)  # Increase the worm size
                score += food.get_score()  # Add points based on the food's color
                food.spawn(worm.points, wall.points, 400, 300)  # Spawn new food
                if len(worm.points) % 4 == 0:
                    wall.next_level()  # Change level every 4 pieces of food
                    level += 1  # Increment the level
                    speed += 1  # Increase the speed of the game

            # Check if the food should disappear
            if food.should_disappear():
                # Spawn new food if it has been on the screen for more than 3 seconds
                food.spawn(worm.points, wall.points, 400, 300)

            # Create the background
            create_background(screen, 400, 300)

            # Draw the game objects
            food.draw(screen)
            wall.draw(screen)
            worm.draw(screen)

            # Display the score and level counters
            score_text = small_font.render(f"Score: {score}", True, (0, 0, 0))
            level_text = small_font.render(f"Level: {level}", True, (0, 0, 0))
            screen.blit(score_text, (10, 5))  # Top-left corner
            screen.blit(level_text, (120, 5))  # Near to the right of the score

            # Update the display
            pygame.display.flip()
            clock.tick(speed)  # Control the game speed

        # Save the score after the game ends
        save_score(user_id, score, level)