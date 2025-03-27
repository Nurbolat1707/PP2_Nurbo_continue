import pygame
import random

pygame.init()


WIDTH, HEIGHT = 500, 600
CAR_WIDTH, CAR_HEIGHT = 50, 80
ROAD_LANES = [150, 250, 350]
COIN_SIZE = 30
SPEED = 5

WHITE = (255, 255, 255)
RED = (200, 0, 0)
YELLOW = (255, 223, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game with Coins")

car_image = pygame.image.load("car.png") 
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

player_x = WIDTH // 2 - CAR_WIDTH // 2
player_y = HEIGHT - CAR_HEIGHT - 20

coins = []
coin_count = 0 

font = pygame.font.Font(None, 36)

running = True
clock = pygame.time.Clock()

def spawn_coin():
    """Generate a new coin at a random lane."""
    lane = random.choice(ROAD_LANES)
    coins.append(pygame.Rect(lane, -COIN_SIZE, COIN_SIZE, COIN_SIZE))

while running:
    clock.tick(30)
    screen.fill(WHITE) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 100:
        player_x -= SPEED
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 100 - CAR_WIDTH:
        player_x += SPEED

    if random.randint(1, 50) == 1:
        spawn_coin()

    for coin in coins[:]:
        coin.y += SPEED
        if coin.y > HEIGHT:
            coins.remove(coin) 

    player_rect = pygame.Rect(player_x, player_y, CAR_WIDTH, CAR_HEIGHT)
    for coin in coins[:]:
        if player_rect.colliderect(coin):
            coins.remove(coin)
            coin_count += 1 

    screen.blit(car_image, (player_x, player_y))

    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin.x + COIN_SIZE // 2, coin.y + COIN_SIZE // 2), COIN_SIZE // 2)

    score_text = font.render(f"Coins: {coin_count}", True, BLACK)
    screen.blit(score_text, (WIDTH - 120, 10))


    pygame.display.flip()

pygame.quit()