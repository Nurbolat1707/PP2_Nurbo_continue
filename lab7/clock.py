import pygame
import sys
import time
from datetime import datetime


pygame.init()
WIDTH, HEIGHT = 900, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

background = pygame.image.load("clock.png")
right_hand = pygame.image.load("rightarm.png") 
left_hand = pygame.image.load("leftarm.png")

background = pygame.transform.scale(background, (WIDTH, HEIGHT))

def rotate_image(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    now = datetime.now()
    seconds = now.second
    minutes = now.minute


    sec_angle = -seconds * 6
    min_angle = -minutes * 6 

    sec_hand, sec_rect = rotate_image(left_hand, sec_angle, (WIDTH//2, HEIGHT//2))
    min_hand, min_rect = rotate_image(right_hand, min_angle, (WIDTH//2, HEIGHT//2))

    screen.blit(sec_hand, sec_rect.topleft)
    screen.blit(min_hand, min_rect.topleft)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(1) 
