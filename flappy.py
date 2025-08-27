import pygame
import random
import sys
import os
 
# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game variables
gravity = 0.5
bird_movement = 0
game_active = True
score = 0
new_high = False  # track if new high score achieved

# Load high score from file
def load_high_score():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            return int(file.read())
    return 0

# Save high score to file
def save_high_score(high_score):
    with open("highscore.txt", "w") as file:
        file.write(str(high_score))

high_score = load_high_score()

# Fonts
font = pygame.font.Font(pygame.font.get_default_font(), 32)
font_big = pygame.font.Font(pygame.font.get_default_font(), 40)

# Bird
bird_surface = pygame.Surface((34, 24))
bird_surface.fill(YELLOW)  # Yellow bird
bird_rect = bird_surface.get_rect(center=(100, HEIGHT // 2))

# Pipes
pipe_width = 60
pipe_height = 400
pipe_gap = 150
pipe_list = []

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)


def create_pipe():
    height = random.randint(150, 450)
    bottom_pipe = pygame.Rect(WIDTH, height, pipe_width, pipe_height)
    top_pipe = pygame.Rect(WIDTH, height - pipe_height - pipe_gap, pipe_width, pipe_height)
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
    return [pipe for pipe in pipes if pipe.right > -50]


def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= HEIGHT:
        return False
    return True


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = font.render(str(int(score)), True, WHITE)
        score_rect = score_surface.get_rect(center=(WIDTH // 2, 50))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = font.render(f'Score: {int(score)}', True, WHITE)
        score_rect = score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
        screen.blit(score_surface, score_rect)

        high_score_surface = font.render(f'High Score: {int(high_score)}', True, WHITE)
        high_score_rect = high_score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(high_score_surface, high_score_rect)

        if new_high:  # Show banner when new high score is achieved
            banner_surface = font_big.render("NEW HIGH SCORE!", True, (255, 215, 0))  # Gold text
            banner_rect = banner_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
            screen.blit(banner_surface, banner_rect)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score(high_score)  # Save before quitting
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 8
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, HEIGHT // 2)
                bird_movement = 0
                score = 0
                new_high = False  # Reset new high flag

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.fill(BLUE)

    if game_active:
        # Bird
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision
        game_active = check_collision(pipe_list)

        # Score
        for pipe in pipe_list:
            if pipe.centerx == bird_rect.centerx:
                score += 0.5
        score_display('main_game')
    else:
        if score > high_score:
            high_score = score
            save_high_score(high_score)
            new_high = True  # Mark that player broke record
        score_display('game_over')

    pygame.display.update()
    clock.tick(FPS)
