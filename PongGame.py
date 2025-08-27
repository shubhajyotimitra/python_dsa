import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball setup
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Paddle setup
player = pygame.Rect(WIDTH-20, HEIGHT//2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT//2 - 70, 10, 140)
player_speed = 0
opponent_speed = 7

# Score
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 50)

# Game variables
MAX_SCORE = 10
game_over = False
winner = ""

clock = pygame.time.Clock()

# Reset ball after scoring
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_over:  # allow movement only if game not finished
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_speed = -7
                if event.key == pygame.K_DOWN:
                    player_speed = 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_speed = 0

    if not game_over:
        # Move ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Collision with top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        # Collision with paddles
        if ball.colliderect(player) or ball.colliderect(opponent):
            ball_speed_x *= -1

        # Score update
        if ball.left <= 0:
            player_score += 1
            if player_score >= MAX_SCORE:
                game_over = True
                winner = "Player"
            reset_ball()
        if ball.right >= WIDTH:
            opponent_score += 1
            if opponent_score >= MAX_SCORE:
                game_over = True
                winner = "Opponent"
            reset_ball()

        # Move player
        player.y += player_speed
        if player.top <= 0:
            player.top = 0
        if player.bottom >= HEIGHT:
            player.bottom = HEIGHT

        # Opponent AI movement
        if opponent.top < ball.y:
            opponent.y += opponent_speed
        if opponent.bottom > ball.y:
            opponent.y -= opponent_speed

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    player_text = font.render(str(player_score), True, WHITE)
    screen.blit(player_text, (WIDTH//2 + 20, 20))

    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(opponent_text, (WIDTH//2 - 60, 20))

    # Show winner if game over
    if game_over:
        win_text = font.render(f"{winner} Wins!", True, WHITE)
        screen.blit(win_text, (WIDTH//2 - 100, HEIGHT//2))

    pygame.display.flip()
    clock.tick(60)

