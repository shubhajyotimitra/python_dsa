import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dragon Cursor 🐉")

# Load your dragon image (make sure it's in same folder)
dragon_img = pygame.image.load("dragon.png")
dragon_img = pygame.transform.scale(dragon_img, (64, 64))  # Resize dragon

# Hide the default mouse cursor
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill background
    screen.fill((30, 30, 30))

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw dragon at mouse position
    screen.blit(dragon_img, (mouse_x, mouse_y))

    # Update display
    pygame.display.update()
    clock.tick(60)
