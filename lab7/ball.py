import pygame

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 25
MOVE_STEP = 20
WHITE, RED = (255, 255, 255), (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

# Ball Initialization
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

def draw_ball():
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - BALL_RADIUS - MOVE_STEP >= 0:
                ball_y -= MOVE_STEP
            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS + MOVE_STEP <= HEIGHT:
                ball_y += MOVE_STEP
            elif event.key == pygame.K_LEFT and ball_x - BALL_RADIUS - MOVE_STEP >= 0:
                ball_x -= MOVE_STEP
            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS + MOVE_STEP <= WIDTH:
                ball_x += MOVE_STEP
    
    draw_ball()
    clock.tick(30)

pygame.quit()