import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY = (135, 206, 235)
GREEN = (0, 200, 0)

# Game variables
gravity = 0.5
bird_movement = 0
score = 0
high_score = 0
game_active = True

# Load fonts
font = pygame.font.Font(None, 50)

# Bird
bird = pygame.Rect(100, HEIGHT//2 - 15, 30, 30)

# Pipes
pipe_width = 60
pipe_height = 400
pipe_gap = 150
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)  # spawn new pipe every 1.5 sec

def create_pipe():
    height = random.randint(200, 400)
    bottom_pipe = pygame.Rect(WIDTH, height, pipe_width, HEIGHT-height)
    top_pipe = pygame.Rect(WIDTH, height - pipe_gap - pipe_height, pipe_width, pipe_height)
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.x -= 5
    return [pipe for pipe in pipes if pipe.right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            return False
    if bird.top <= 0 or bird.bottom >= HEIGHT:
        return False
    return True

# Score display
def display_score(game_state):
    if game_state == "main_game":
        score_surface = font.render(str(score), True, WHITE)
        screen.blit(score_surface, (WIDTH//2 - 10, 20))
    if game_state == "game_over":
        score_surface = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surface, (WIDTH//2 - 60, HEIGHT//2 - 50))

        high_score_surface = font.render(f"High Score: {high_score}", True, WHITE)
        screen.blit(high_score_surface, (WIDTH//2 - 100, HEIGHT//2))

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 10
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird.center = (100, HEIGHT//2)
                bird_movement = 0
                score = 0
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.fill(SKY)

    if game_active:
        # Bird movement
        bird_movement += gravity
        bird.y += int(bird_movement)
        pygame.draw.ellipse(screen, (255, 255, 0), bird)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision
        game_active = check_collision(pipe_list)

        # Score
        for pipe in pipe_list:
            if pipe.centerx == bird.centerx:
                score += 1
        display_score("main_game")

    else:
        high_score = max(score, high_score)
        display_score("game_over")

    pygame.display.update()
    clock.tick(60)
