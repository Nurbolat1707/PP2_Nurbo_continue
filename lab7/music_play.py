import pygame
import keyboard

pygame.mixer.init()

playlist = ["Attention.mp3", "Суу.mp3", "la la la.mp3"]
current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

print("Press 'p' to play, 's' to stop, 'n' for next, 'b' for previous.")
while True:
    if keyboard.is_pressed('p'):
        play_music()
    elif keyboard.is_pressed('s'):
        stop_music()
    elif keyboard.is_pressed('n'):
        next_track()
    elif keyboard.is_pressed('b'):
        previous_track()
    elif keyboard.is_pressed('q'):
        print("Exciting...")
        break

pygame.quit()
