import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color = BLACK
brush_size = 5
tool = "brush" 

running = True
mouse_down = False
start_pos = None 

while running:
    screen.blit(canvas, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_p:
                tool = "brush"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_t:
                tool = "rectangle"

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            end_pos = event.pos
            if tool == "rectangle":
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                pygame.draw.rect(canvas, color, rect, 2)
            elif tool == "circle":
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2) ** 0.5 / 2)
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(canvas, color, center, radius, 2)

        elif event.type == pygame.MOUSEMOTION and mouse_down:
            if tool == "brush":
                pygame.draw.circle(canvas, color, event.pos, brush_size)
            elif tool == "eraser":
                pygame.draw.circle(canvas, WHITE, event.pos, brush_size)

    pygame.display.flip()

pygame.quit()
