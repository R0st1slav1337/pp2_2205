import pygame
import os
from pygame.locals import *

# Initialize pygame mixer
pygame.mixer.init()

# Initialize pygame
pygame.init()

# Define music player class
class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        # Get a list of all mp3 files in the music folder
        self.playlist = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith('.mp3')]
        self.current_track = 0
        self.is_playing = False
        self.volume = 0.3  # Initial volume (30%)
        pygame.mixer.music.set_volume(self.volume)

    def play(self):
        if not self.is_playing:
            pygame.mixer.music.load(self.playlist[self.current_track]) # Load the current track
            pygame.mixer.music.play()
            self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next(self):
        self.stop()
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.play()

    def previous(self): 
        self.stop()
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.play()

    def increase_volume(self):
        self.volume = min(self.volume + 0.1, 1.0)  # Increase volume by 10%, max 100%
        pygame.mixer.music.set_volume(self.volume)

    def decrease_volume(self):
        self.volume = max(self.volume - 0.1, 0.0)  # Decrease volume by 10%, min 0%
        pygame.mixer.music.set_volume(self.volume)

    def get_current_track_name(self):
        return os.path.basename(self.playlist[self.current_track])

# Create music player instance
music_folder = 'week7/music'
player = MusicPlayer(music_folder)

# Set up the display
width, height = 600, 250
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Music Player')

# Define font
font = pygame.font.SysFont(None, 36)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_c:  # Play
                player.play()
            elif event.key == K_v:  # Stop
                player.stop()
            elif event.key == K_n:  # Next
                player.next()
            elif event.key == K_b:  # Previous
                player.previous()
            elif event.key == K_UP:  # Increase volume
                player.increase_volume()
            elif event.key == K_DOWN:  # Decrease volume
                player.decrease_volume()

    # Clear the window
    window.fill((255, 255, 255))

    # Display current track
    current_track_text = font.render(f"Current track: {player.get_current_track_name()}", True, (0, 0, 0))
    window.blit(current_track_text, (20, 20))

    # Display controls
    controls_text = [
        "Press 'C' to Play",
        "Press 'V' to Stop",
        "Press 'B' for Previous",
        "Press 'N' for Next",
        "Press 'UP' to increase volume",
        "Press 'DOWN' to decrease volume"
    ]
    for i, text in enumerate(controls_text):
        control_text = font.render(text, True, (0, 0, 0))
        window.blit(control_text, (20, 60 + i * 30))

    # Update the display
    pygame.display.flip()

pygame.quit()