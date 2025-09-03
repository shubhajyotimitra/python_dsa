import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dragon Animation 🐉")

clock = pygame.time.Clock()

# Load dragon sprites (place PNGs in the same folder as this script)
dragon_head = pygame.image.load("assets/dragon_head.png").convert_alpha()
dragon_scale = pygame.image.load("assets/dragon_scale.png").convert_alpha()

# Scale the images for performance
dragon_head = pygame.transform.scale(dragon_head, (60, 60))
dragon_scale = pygame.transform.scale(dragon_scale, (35, 35))

# Settings
N = 25  # number of body segments
rad = 0.5
frm = 0
elems = [{"x": WIDTH // 2, "y": HEIGHT // 2} for _ in range(N)]
pointer = {"x": WIDTH // 2, "y": HEIGHT // 2}

def run():
    global frm
    running = True
    while running:
        screen.fill((20, 20, 30))  # dark background for contrast

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update pointer with mouse position
        mx, my = pygame.mouse.get_pos()
        pointer["x"], pointer["y"] = mx, my

        # --- Head logic ---
        e = elems[0]
        ax = (math.cos(3 * frm) * rad * WIDTH) / HEIGHT
        ay = (math.sin(4 * frm) * rad * HEIGHT) / WIDTH

        e["x"] += (ax + pointer["x"] - e["x"]) / 10
        e["y"] += (ay + pointer["y"] - e["y"]) / 10

        # Angle for head rotation
        angle = 0
        if N > 1:
            ep = elems[1]
            angle = math.degrees(math.atan2(ep["y"] - e["y"], ep["x"] - e["x"]))

        rotated_head = pygame.transform.rotate(dragon_head, -angle)
        rect = rotated_head.get_rect(center=(e["x"], e["y"]))
        screen.blit(rotated_head, rect.topleft)

        # --- Body logic ---
        for i in range(1, N):
            e = elems[i]
            ep = elems[i - 1]
            a = math.atan2(e["y"] - ep["y"], e["x"] - ep["x"])

            # Smooth trailing effect
            e["x"] += (ep["x"] - e["x"] + (math.cos(a) * (100 - i)) / 5) / 4
            e["y"] += (ep["y"] - e["y"] + (math.sin(a) * (100 - i)) / 5) / 4

            # Rotate body scale image
            rotated_scale = pygame.transform.rotate(dragon_scale, -math.degrees(a))
            rect = rotated_scale.get_rect(center=(e["x"], e["y"]))
            screen.blit(rotated_scale, rect.topleft)

        frm += 0.05
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# Run the game loop
run()
