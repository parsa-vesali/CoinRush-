import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coin & Obstacle Game 🪙")

# Colors
white = (248, 250, 252)
black = (2, 6, 23)
sky = (2, 132, 199)
yellow = (250, 204, 21)
dark_gray = (107, 114, 128)
light_gray = (209, 213, 219)

# Player setup
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 10

# Obstacle setup
obstacle_width = 100
obstacle_height = 20
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3
obstacle_speed_increase = 0.2

# Coin setup
coin_radius = 15
coin_x = random.randint(coin_radius, screen_width - coin_radius)
coin_y = -coin_radius
coin_speed = 4
coin_speed_increase = 0.2

# Game variables
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 80)
game_over = False
running = True
dark_mode = True  # toggle background theme

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Restart game on Enter key if game is over
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                player_x = screen_width // 2 - player_width // 2
                obstacle_x = random.randint(0, screen_width - obstacle_width)
                obstacle_y = -obstacle_height
                obstacle_speed = 3
                coin_x = random.randint(coin_radius, screen_width - coin_radius)
                coin_y = -coin_radius
                coin_speed = 4
                score = 0

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        # Move obstacle
        obstacle_y += obstacle_speed
        if obstacle_y > screen_height:
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            obstacle_y = -obstacle_height
            obstacle_speed += obstacle_speed_increase

        # Move coin
        coin_y += coin_speed
        if coin_y > screen_height:
            coin_x = random.randint(coin_radius, screen_width - coin_radius)
            coin_y = -coin_radius
            coin_speed += coin_speed_increase

        # Check collision with obstacle
        if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x and \
                player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
            game_over = True

        # Check collision with coin
        if player_x < coin_x + coin_radius and player_x + player_width > coin_x - coin_radius and \
                player_y < coin_y + coin_radius and player_y + player_height > coin_y - coin_radius:
            score += 10
            coin_x = random.randint(coin_radius, screen_width - coin_radius)
            coin_y = -coin_radius
            coin_speed += coin_speed_increase

    # Draw background
    screen.fill(black if dark_mode else white)

    if game_over:
        # Display Game Over screen
        game_over_text = game_over_font.render("Game Over!", True, light_gray)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2,
                                     screen_height // 2 - game_over_text.get_height() // 2))

        restart_text = font.render("Press Enter to play again!", True, light_gray)
        screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2,
                                   screen_height // 2 + 40))

        final_score_text = font.render(f"Final Score: {score}", True, light_gray)
        screen.blit(final_score_text, (screen_width // 2 - final_score_text.get_width() // 2,
                                       screen_height // 2 + 80))
    else:
        # Draw player, obstacle, coin, and score
        pygame.draw.rect(screen, light_gray, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, sky, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        pygame.draw.circle(screen, yellow, (coin_x, coin_y), coin_radius)
        score_text = font.render(f"Score: {score}", True, light_gray)
        screen.blit(score_text, (10, 10))

    # Update screen and tick clock
    pygame.display.update()
    clock.tick(60)

pygame.quit()
