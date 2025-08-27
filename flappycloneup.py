import pygame
import sys
import random
import os

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Load assets from assets/ folder
ASSET_PATH = "assets/"

bg_img = pygame.image.load("assets/background.png")

bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

bird_img = pygame.image.load(os.path.join(ASSET_PATH, "bird.png"))
bird_img = pygame.transform.scale(bird_img, (40, 30))

pipe_img = pygame.image.load(os.path.join(ASSET_PATH, "pipe.png"))
pipe_img = pygame.transform.scale(pipe_img, (70, 400))

# Sounds
flap_sound = pygame.mixer.Sound(os.path.join(ASSET_PATH, "flap.wav"))
hit_sound = pygame.mixer.Sound(os.path.join(ASSET_PATH, "hit.wav"))
point_sound = pygame.mixer.Sound(os.path.join(ASSET_PATH, "point.wav"))

# Fonts
font = pygame.font.Font(None, 50)

# Game variables
gravity = 0.5
bird_movement = 0
score = 0
high_score = 0
game_active = True

# Bird rect
bird = bird_img.get_rect(center=(100, HEIGHT // 2))

# Pipes
pipe_gap = 150
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)

# High score persistence
def load_high_score():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            return int(file.read())
    return 0

def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

high_score = load_high_score()

def create_pipe():
    height = random.randint(200, 400)
    bottom_pipe = pipe_img.get_rect(midtop=(WIDTH + 50, height))
    top_pipe = pipe_img.get_rect(midbottom=(WIDTH + 50, height - pipe_gap))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return [pipe for pipe in pipes if pipe.right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= HEIGHT:  # bottom pipe
            screen.blit(pipe_img, pipe)
        else:  # top pipe (flipped)
            flip_pipe = pygame.transform.flip(pipe_img, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            hit_sound.play()
            return False
    if bird.top <= 0 or bird.bottom >= HEIGHT:
        hit_sound.play()
        return False
    return True

def display_score(game_state):
    if game_state == "main_game":
        score_surface = font.render(str(score), True, WHITE)
        screen.blit(score_surface, (WIDTH // 2 - 10, 20))
    if game_state == "game_over":
        score_surface = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surface, (WIDTH // 2 - 60, HEIGHT // 2 - 50))

        high_score_surface = font.render(f"High Score: {high_score}", True, WHITE)
        screen.blit(high_score_surface, (WIDTH // 2 - 100, HEIGHT // 2))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score(high_score)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 10
                flap_sound.play()
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird.center = (100, HEIGHT // 2)
                bird_movement = 0
                score = 0
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    # Draw background
    screen.blit(bg_img, (0, 0))

    if game_active:
        # Bird movement
        bird_movement += gravity
        bird.centery += int(bird_movement)
        screen.blit(bird_img, bird)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision
        game_active = check_collision(pipe_list)

        # Score
        for pipe in pipe_list:
            if pipe.centerx == bird.centerx:
                score += 1
                point_sound.play()
        display_score("main_game")

    else:
        high_score = max(score, high_score)
        display_score("game_over")

    pygame.display.update()
    clock.tick(FPS)
