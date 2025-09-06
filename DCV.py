import os
import math
import random
import pygame

# ---------------------------
# Config
# ---------------------------
WIDTH, HEIGHT = 900, 600
BG_COLOR = (18, 18, 22)
SMOOTHING = 0.18     # Follow speed (0..1), higher = snappier
FIRE_COOLDOWN = 0.12 # Seconds between fire particles while holding click
TRAIL_RATE = 0.02    # Seconds between tail particles
MAX_PARTICLES = 800

ASSET_FILE = "dragon.png"  # Optional: drop a transparent dragon sprite in same folder

# ---------------------------
# Helpers
# ---------------------------
def lerp(a, b, t):
    return a + (b - a) * t

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

# ---------------------------
# Fallback "vector dragon" sprite generator
# ---------------------------
def make_vector_dragon(size=120, wing_phase=0.0):
    """
    Draws a simple stylized dragon on a transparent surface.
    The wing_phase animates the wing flap.
    """
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    cx, cy = size // 2, size // 2

    # Colors
    body = (60, 200, 120, 255)
    belly = (200, 255, 220, 220)
    horn = (230, 230, 230, 255)
    eye = (10, 10, 10, 255)
    wing = (80, 240, 160, 200)

    # Body (rounded)
    pygame.draw.ellipse(surf, body, (size*0.15, size*0.35, size*0.55, size*0.35))

    # Belly
    pygame.draw.ellipse(surf, belly, (size*0.22, size*0.45, size*0.38, size*0.22))

    # Head
    pygame.draw.ellipse(surf, body, (size*0.55, size*0.35, size*0.32, size*0.26))

    # Horn
    pygame.draw.polygon(
        surf, horn,
        [
            (size*0.78, size*0.33),
            (size*0.86, size*0.18),
            (size*0.82, size*0.36),
        ]
    )

    # Eye
    pygame.draw.circle(surf, eye, (int(size*0.76), int(size*0.47)), max(1, size//25))

    # Tail
    pygame.draw.polygon(
        surf, body,
        [
            (size*0.15, size*0.52),
            (size*0.05, size*0.48),
            (size*0.12, size*0.56),
        ]
    )

    # Animated wing (flaps up & down with phase)
    flap = math.sin(wing_phase) * size*0.10
    wing_pts = [
        (size*0.44, size*0.37),
        (size*0.28, size*0.22 + flap),
        (size*0.22, size*0.40 + flap*0.5),
        (size*0.40, size*0.45),
    ]
    pygame.draw.polygon(surf, wing, wing_pts)

    return surf

# ---------------------------
# Fire & trail particles
# ---------------------------
class Particle:
    __slots__ = ("x","y","vx","vy","life","max_life","radius","color","gravity")
    def __init__(self, x, y, vx, vy, life, radius, color, gravity=0.0):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.life = life
        self.max_life = life
        self.radius = radius
        self.color = color
        self.gravity = gravity

    def update(self, dt):
        self.vy += self.gravity * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.life -= dt
        return self.life > 0

    def draw(self, surf):
        if self.life <= 0: return
        alpha = clamp(int(255 * (self.life / self.max_life)), 0, 255)
        c = (*self.color[:3], alpha)
        pygame.draw.circle(surf, c, (int(self.x), int(self.y)), max(1, int(self.radius)))

# ---------------------------
# Main
# ---------------------------
def main():
    pygame.init()
    flags = pygame.SCALED | pygame.RESIZABLE
    screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
    pygame.display.set_caption("Dragon Cursor (Pygame)")
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    # Load sprite or use fallback
    dragon_img = None
    if os.path.exists(ASSET_FILE):
        img = pygame.image.load(ASSET_FILE).convert_alpha()
        # Scale to a nice size based on window height
        scale_h = max(80, min(160, screen.get_height() * 0.18))
        scale = scale_h / img.get_height()
        dragon_img = pygame.transform.smoothscale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))

    # State
    pos = pygame.Vector2(WIDTH/2, HEIGHT/2)
    vel = pygame.Vector2(0, 0)
    wing_phase = 0.0
    particles = []
    last_fire = 0.0
    last_trail = 0.0
    hold_fire = False
    full_screen = False

    # For rotation
    last_draw_pos = pos.xy

    running = True
    t = 0.0

    while running:
        dt = clock.tick(120) / 1000.0
        t += dt
        screen.fill(BG_COLOR)

        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                elif e.key == pygame.K_f:
                    full_screen = not full_screen
                    if full_screen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.SCALED)
                    else:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.RESIZABLE)
                    pygame.mouse.set_visible(False)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:  # left click
                    hold_fire = True
                elif e.button in (3, 4):  # right or wheel up -> flap burst
                    for _ in range(25):
                        ang = random.uniform(0, math.tau)
                        spd = random.uniform(40, 160)
                        particles.append(Particle(
                            pos.x, pos.y,
                            math.cos(ang)*spd, math.sin(ang)*spd,
                            life=random.uniform(0.3, 0.7),
                            radius=random.uniform(2.0, 4.0),
                            color=(140, 255, 200),
                            gravity=50.0
                        ))
            elif e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    hold_fire = False

        # Mouse target & smoothing
        mx, my = pygame.mouse.get_pos()
        target = pygame.Vector2(mx, my)

        # Smooth follow
        before = pos.copy()
        pos.x = lerp(pos.x, target.x, SMOOTHING)
        pos.y = lerp(pos.y, target.y, SMOOTHING)
        vel = (pos - before) / dt if dt > 0 else pygame.Vector2(0, 0)

        # Wing animation (faster when moving)
        speed = vel.length()
        wing_phase += dt * (6.0 + clamp(speed / 70.0, 0.0, 10.0))

        # Leave a faint trail
        last_trail += dt
        if last_trail >= TRAIL_RATE:
            last_trail = 0.0
            if len(particles) < MAX_PARTICLES:
                particles.append(Particle(
                    pos.x, pos.y,
                    vx=random.uniform(-15, 15),
                    vy=random.uniform(-15, 15),
                    life=random.uniform(0.4, 0.9),
                    radius=random.uniform(2.0, 5.0),
                    color=(120, 200, 150),
                    gravity=0.0
                ))

        # Fire breath when holding left click
        last_fire += dt
        if hold_fire and last_fire >= FIRE_COOLDOWN:
            last_fire = 0.0
            # Direction from previous draw pos to current (face movement)
            dir_vec = pygame.Vector2(1, 0)
            move = pos - pygame.Vector2(last_draw_pos)
            if move.length_squared() > 1e-3:
                dir_vec = move.normalize()
            muzzle = pos + dir_vec * 40
            for _ in range(12):
                ang_off = random.uniform(-0.2, 0.2)
                spd = random.uniform(220, 360)
                dir2 = dir_vec.rotate_rad(ang_off)
                col = random.choice([(255, 120, 40), (255, 180, 60), (255, 220, 120)])
                particles.append(Particle(
                    muzzle.x, muzzle.y,
                    dir2.x*spd, dir2.y*spd,
                    life=random.uniform(0.25, 0.55),
                    radius=random.uniform(2.0, 5.0),
                    color=col,
                    gravity=70.0
                ))

        # Update & draw particles
        new_particles = []
        for p in particles:
            if p.update(dt):
                new_particles.append(p)
        particles = new_particles[-MAX_PARTICLES:]

        for p in particles:
            p.draw(screen)

        # Draw dragon (rotated toward movement)
        draw_pos = (int(pos.x), int(pos.y))
        angle_deg = 0.0
        delta = pos - pygame.Vector2(last_draw_pos)
        if delta.length_squared() > 1e-3:
            angle_deg = math.degrees(math.atan2(delta.y, delta.x))
        last_draw_pos = pos.xy

        if dragon_img:
            # Slight bob with wing phase
            bob = math.sin(wing_phase*0.5) * 3
            rotated = pygame.transform.rotozoom(dragon_img, -angle_deg, 1.0 + math.sin(wing_phase)*0.02)
            rect = rotated.get_rect(center=(draw_pos[0], draw_pos[1] + bob))
            screen.blit(rotated, rect)
        else:
            # Fallback vector dragon
            vec = make_vector_dragon(size=120, wing_phase=wing_phase)
            vec = pygame.transform.rotozoom(vec, -angle_deg, 1.0)
            rect = vec.get_rect(center=draw_pos)
            screen.blit(vec, rect)

        # Minimal HUD
        font = pygame.font.SysFont(None, 18)
        tip = "Move mouse • Left click: Fire • Right click: Flap • F: Fullscreen • Esc: Quit"
        text = font.render(tip, True, (210, 210, 220))
        screen.blit(text, (12, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
