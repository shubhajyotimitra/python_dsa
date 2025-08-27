import pygame
import sys
import random
import os

# ---------- Setup ----------
pygame.init()
WIDTH, HEIGHT = 600, 600
CELL = 20
GRID_W, GRID_H = WIDTH // CELL, HEIGHT // CELL

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Colors
BG = (18, 18, 18)
GRID = (30, 30, 30)
SNAKE = (80, 200, 120)
HEAD = (100, 255, 160)
FOOD = (240, 80, 80)
TEXT = (240, 240, 240)
GOLD = (255, 215, 0)

FONT = pygame.font.Font(pygame.font.get_default_font(), 28)
FONT_BIG = pygame.font.Font(pygame.font.get_default_font(), 42)

# Sounds (optional; wrapped in try so game works without mixer)
eat_sound = None
try:
    pygame.mixer.init()
    # Very short generated “click” using Sound(buffer) would be overkill; skip file deps.
    # Keep as None; you can drop a WAV named eat.wav in the same folder and uncomment below.
    # eat_sound = pygame.mixer.Sound("eat.wav")
except Exception:
    pass

# ---------- High Score ----------
def load_high():
    if os.path.exists("snake_highscore.txt"):
        try:
            return int(open("snake_highscore.txt").read().strip())
        except Exception:
            return 0
    return 0

def save_high(v):
    try:
        with open("snake_highscore.txt", "w") as f:
            f.write(str(v))
    except Exception:
        pass

high_score = load_high()

# ---------- Helpers ----------
def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, GRID, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, GRID, (0, y), (WIDTH, y))

def draw_cell(pos, color):
    x, y = pos
    r = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
    pygame.draw.rect(screen, color, r)

def random_empty_cell(snake_body):
    while True:
        p = (random.randint(0, GRID_W - 1), random.randint(0, GRID_H - 1))
        if p not in snake_body:
            return p

# ---------- Game State ----------
def reset_game():
    start = (GRID_W // 2, GRID_H // 2)
    snake = [start, (start[0] - 1, start[1]), (start[0] - 2, start[1])]
    direction = (1, 0)  # moving right
    food = random_empty_cell(snake)
    score = 0
    speed = 10  # base FPS; increases as you eat
    new_high = False
    paused = False
    return snake, direction, food, score, speed, new_high, paused

snake, direction, food, score, speed, new_high, paused = reset_game()
pending_dir = direction  # to avoid reversing twice in a tick

MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 120)  # movement tick; FPS still caps drawing

# ---------- Main Loop ----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high(high_score)
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                if direction != (0, 1): pending_dir = (0, -1)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                if direction != (0, -1): pending_dir = (0, 1)
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                if direction != (1, 0): pending_dir = (-1, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                if direction != (-1, 0): pending_dir = (1, 0)
            elif event.key in (pygame.K_p, pygame.K_SPACE):
                paused = not paused
            elif event.key == pygame.K_r:
                snake, direction, food, score, speed, new_high, paused = reset_game()

        if event.type == MOVE_EVENT and not paused:
            # apply direction chosen since last move
            direction = pending_dir

            # move head
            hx, hy = snake[0]
            nx, ny = hx + direction[0], hy + direction[1]

            # wall collision (classic rules)
            if nx < 0 or nx >= GRID_W or ny < 0 or ny >= GRID_H:
                # game over -> reset flag to show banner if new high
                if score > high_score:
                    high_score = score
                    save_high(high_score)
                    new_high = True
                paused = True  # freeze on game over screen
            else:
                new_head = (nx, ny)

                # self collision
                if new_head in snake:
                    if score > high_score:
                        high_score = score
                        save_high(high_score)
                        new_high = True
                    paused = True
                else:
                    snake.insert(0, new_head)

                    # eating
                    if new_head == food:
                        score += 1
                        # if eat_sound: eat_sound.play()
                        food = random_empty_cell(snake)
                        # speed up subtly every 3 points (cap to keep playable)
                        if score % 3 == 0 and speed < 22:
                            speed += 1
                    else:
                        snake.pop()

    # ---------- Draw ----------
    screen.fill(BG)
    draw_grid()

    # food
    draw_cell(food, FOOD)

    # snake
    for i, seg in enumerate(snake):
        draw_cell(seg, HEAD if i == 0 else SNAKE)

    # UI
    score_surf = FONT.render(f"Score: {score}", True, TEXT)
    hs_surf =    FONT.render(f"High: {high_score}", True, TEXT)
    screen.blit(score_surf, (12, 10))
    screen.blit(hs_surf, (WIDTH - hs_surf.get_width() - 12, 10))

    if paused:
        title = "PAUSED" if snake else "SNAKE"
        over = FONT_BIG.render("Game Over", True, TEXT)
        tip  = FONT.render("Press R to Restart, P/Space to Pause/Resume", True, TEXT)
        screen.blit(over, (WIDTH//2 - over.get_width()//2, HEIGHT//2 - 60))
        screen.blit(tip,  (WIDTH//2 - tip.get_width()//2, HEIGHT//2))
        if new_high:
            nh = FONT_BIG.render("NEW HIGH SCORE!", True, GOLD)
            screen.blit(nh, (WIDTH//2 - nh.get_width()//2, HEIGHT//2 + 50))

    pygame.display.flip()
    clock.tick(speed)  # caps draw rate; movement uses MOVE_EVENT
