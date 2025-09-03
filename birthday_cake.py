# birthday_cake.py
# Animated birthday cake using Pygame
# Requires: pip install pygame

import pygame
import random
import math
from pygame import gfxdraw

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Birthday! 🎂")
clock = pygame.time.Clock()

# Colors
BG = (28, 30, 34)
CAKE_BROWN = (115, 74, 48)
FROSTING = (245, 220, 230)
CANDLE_COLORS = [(200, 40, 40), (40, 120, 200), (40, 200, 120), (200, 140, 20)]
FLAME_OUTER = (255, 200, 50)
FLAME_INNER = (255, 120, 20)
TEXT_COL = (250, 250, 250)
CONFETTI_COLS = [(239, 71, 111), (255, 209, 102), (6, 214, 160), (17, 138, 178), (7, 59, 76)]

# Cake geometry
cake_w = 520
cake_h = 220
cake_x = (WIDTH - cake_w) // 2
cake_y = HEIGHT - cake_h - 60

# Candle settings
num_candles = 7
candle_spacing = cake_w // (num_candles + 1)
candle_width = 12
candle_height = 40

# Confetti particles
confetti = []
for _ in range(90):
    confetti.append({
        "x": random.uniform(0, WIDTH),
        "y": random.uniform(-HEIGHT, 0),
        "vy": random.uniform(1.0, 3.5),
        "vx": random.uniform(-0.5, 0.5),
        "size": random.randint(4, 8),
        "col": random.choice(CONFETTI_COLS),
        "angle": random.uniform(0, math.pi*2),
        "spin": random.uniform(-0.15, 0.15)
    })

# Candle data
candles = []
for i in range(num_candles):
    cx = cake_x + (i + 1) * candle_spacing
    # position them near top of cake frosting
    cy = cake_y + 30
    phase = random.uniform(0, math.pi*2)
    candles.append({"x": cx, "y": cy, "phase": phase, "color": random.choice(CANDLE_COLORS)})

font_big = pygame.font.SysFont("arial", 48, bold=True)
font_small = pygame.font.SysFont("arial", 28, bold=False)

def draw_round_rect(surface, rect, color, radius=12):
    x, y, w, h = rect
    gfxdraw.aacircle(surface, x+radius, y+radius, radius, color)
    gfxdraw.filled_circle(surface, x+radius, y+radius, radius, color)
    gfxdraw.aacircle(surface, x+w-radius-1, y+radius, radius, color)
    gfxdraw.filled_circle(surface, x+w-radius-1, y+radius, radius, color)
    gfxdraw.aacircle(surface, x+radius, y+h-radius-1, radius, color)
    gfxdraw.filled_circle(surface, x+radius, y+h-radius-1, radius, color)
    gfxdraw.aacircle(surface, x+w-radius-1, y+h-radius-1, radius, color)
    gfxdraw.filled_circle(surface, x+w-radius-1, y+h-radius-1, radius, color)
    pygame.draw.rect(surface, color, (x+radius, y, w-2*radius, h))
    pygame.draw.rect(surface, color, (x, y+radius, w, h-2*radius))

def draw_cake():
    # shadow under cake
    shadow_rect = (cake_x+10, cake_y + cake_h - 10, cake_w - 20, 20)
    pygame.draw.ellipse(screen, (20,20,20), shadow_rect)

    # bottom layer
    bottom = (cake_x, cake_y + 100, cake_w, 120)
    draw_round_rect(screen, bottom, CAKE_BROWN, radius=18)
    # middle frosting strip
    middle_frost = (cake_x+10, cake_y + 70, cake_w-20, 40)
    draw_round_rect(screen, middle_frost, FROSTING, radius=14)
    # top smaller layer
    top = (cake_x+60, cake_y + 30, cake_w-120, 70)
    draw_round_rect(screen, top, CAKE_BROWN, radius=14)
    # top frosting
    top_frost = (cake_x+70, cake_y + 20, cake_w-140, 20)
    draw_round_rect(screen, top_frost, FROSTING, radius=8)

    # decorative frosting drips (simple arcs)
    for i in range(8):
        rx = cake_x + 30 + i * ((cake_w-60) // 8)
        ry = cake_y + 100
        pygame.draw.ellipse(screen, FROSTING, (rx, ry-10, 28, 22))

def draw_candle(c):
    # simple sway animation using phase
    t = pygame.time.get_ticks() / 1000.0
    sway = math.sin(t*2 + c["phase"]) * 4  # degrees or px
    x = c["x"] + sway
    y = c["y"]

    # candle body
    body_rect = (x - candle_width//2, y - candle_height, candle_width, candle_height)
    pygame.draw.rect(screen, c["color"], body_rect, border_radius=3)

    # candle stripe
    stripe_w = 4
    pygame.draw.rect(screen, (255,255,255), (x - stripe_w//2, y - candle_height//2, stripe_w, candle_height//2), border_radius=2)

    # flame flicker: change size & offset
    flame_jitter = random.uniform(-1.2, 1.2)
    flame_x = x + flame_jitter
    flame_y = y - candle_height - 6 + random.uniform(-1, 1)
    # outer flame
    pygame.draw.polygon(screen, FLAME_OUTER, [
        (flame_x, flame_y),
        (flame_x - 6, flame_y + 18),
        (flame_x + 6, flame_y + 18)
    ])
    # inner flame (smaller)
    pygame.draw.polygon(screen, FLAME_INNER, [
        (flame_x, flame_y + 4),
        (flame_x - 3, flame_y + 15),
        (flame_x + 3, flame_y + 15)
    ])
    # small glow
    glow_radius = 12 + math.sin(pygame.time.get_ticks()/150.0 + c["phase"]) * 2
    s = pygame.Surface((glow_radius*2, glow_radius*2), pygame.SRCALPHA)
    pygame.draw.circle(s, (255,200,100,40), (glow_radius, glow_radius), int(glow_radius))
    screen.blit(s, (flame_x - glow_radius, flame_y - glow_radius + 2))

def update_confetti():
    for p in confetti:
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["angle"] += p["spin"]
        # wrap or reset
        if p["y"] > HEIGHT + 20:
            p["y"] = random.uniform(-120, -10)
            p["x"] = random.uniform(0, WIDTH)
            p["vy"] = random.uniform(1.0, 3.5)
            p["vx"] = random.uniform(-0.5, 0.5)

def draw_confetti():
    for p in confetti:
        rect = pygame.Rect(0, 0, p["size"], p["size"]*0.6)
        rect.center = (p["x"], p["y"])
        # rotate a tiny square by angle
        surf = pygame.Surface(rect.size, pygame.SRCALPHA)
        pygame.draw.rect(surf, p["col"], (0, 0, rect.width, rect.height))
        rsurf = pygame.transform.rotate(surf, math.degrees(p["angle"]))
        screen.blit(rsurf, rsurf.get_rect(center=(p["x"], p["y"])))

def draw_texts():
    # Happy Birthday text
    txt = font_big.render("HAPPY BIRTHDAY!", True, TEXT_COL)
    txt_rect = txt.get_rect(center=(WIDTH//2, 60))
    # shadow
    screen.blit(font_big.render("HAPPY BIRTHDAY!", True, (10,10,10)), txt_rect.move(2,2))
    screen.blit(txt, txt_rect)
    # small instruction
    sub = font_small.render("STAY HAPPY & STAY BLESSED ", True, (220,220,220))
    screen.blit(sub, sub.get_rect(center=(WIDTH//2, 110)))

def main_loop():
    running = True
    # for little candle sparkles
    sparkle_timer = 0
    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # allow space to blow out (toggle flames)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # simple toggle: move all candles off-screen flame flag by setting phase huge
                for c in candles:
                    if "out" in c:
                        c.pop("out")
                    else:
                        c["out"] = True

        screen.fill(BG)

        # draw confetti behind
        draw_confetti()
        update_confetti()

        draw_cake()

        # draw candles
        for i, c in enumerate(candles):
            if c.get("out"):
                # draw unlit wick as tiny dark dot
                x = c["x"]
                y = c["y"] - candle_height
                pygame.draw.circle(screen, (20, 20, 20), (int(x), int(y)), 3)
            else:
                draw_candle(c)

        draw_texts()

        # small glowing stars over cake occasionally
        sparkle_timer += dt
        if sparkle_timer > 0.08:
            sparkle_timer = 0
            for _ in range(2):
                sx = random.uniform(cake_x+80, cake_x + cake_w - 80)
                sy = random.uniform(cake_y + 10, cake_y + cake_h - 40)
                r = random.randint(1, 3)
                pygame.draw.circle(screen, (255, 240, 200), (int(sx), int(sy)), r)

        # footer hint
        hint = font_small.render("Press SPACE to toggle candle flames", True, (180,180,180))
        screen.blit(hint, (10, HEIGHT - 30))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main_loop()
