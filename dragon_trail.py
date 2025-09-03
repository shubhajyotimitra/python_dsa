import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dragon Trail Animation")

clock = pygame.time.Clock()

# Snake/Dragon settings
N = 20  # number of segments
rad = 0.5
frm = 0

# Each element = dictionary with x,y
elems = [{"x": WIDTH // 2, "y": HEIGHT // 2} for _ in range(N)]

# Pointer starts at center
pointer = {"x": WIDTH // 2, "y": HEIGHT // 2}

# Colors
GREEN = (0, 255, 100)
BLACK = (0, 0, 0)


def run():
    global frm
    running = True
    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update pointer with mouse position
        mx, my = pygame.mouse.get_pos()
        pointer["x"], pointer["y"] = mx, my

        # First element (head)
        e = elems[0]
        ax = (math.cos(3 * frm) * rad * WIDTH) / HEIGHT
        ay = (math.sin(4 * frm) * rad * HEIGHT) / WIDTH

        e["x"] += (ax + pointer["x"] - e["x"]) / 10
        e["y"] += (ay + pointer["y"] - e["y"]) / 10

        # Draw head
        pygame.draw.circle(screen, GREEN, (int(e["x"]), int(e["y"])), 12)

        # Rest of the elements (tail)
        for i in range(1, N):
            e = elems[i]
            ep = elems[i - 1]

            a = math.atan2(e["y"] - ep["y"], e["x"] - ep["x"])

            e["x"] += (ep["x"] - e["x"] + (math.cos(a) * (100 - i)) / 5) / 4
            e["y"] += (ep["y"] - e["y"] + (math.sin(a) * (100 - i)) / 5) / 4

            radius = max(3, 12 - i // 2)  # gradually smaller tail
            pygame.draw.circle(screen, GREEN, (int(e["x"]), int(e["y"])), radius)

        # Frame update
        frm += 0.05
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# Run animation
run()
