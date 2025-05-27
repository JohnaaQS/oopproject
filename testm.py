import pygame
import sys
import terrein
# Init
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Mannetje (1 afbeelding)")
blokken = terrein.Blocks()

# Clock
clock = pygame.time.Clock()
FPS = 60

# Kleuren
bg = pygame.image.load('images\Achtergrond.png')

# Mario Klasse
class Mario(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.image.load('images\mario.png').convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right, (50, 60))
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.vel_y = 0
        self.jumping = False
        self.direction = 1  # 1 = rechts, -1 = links

    def update(self, keys):
        dx = 0

        # Bewegen
        if keys[pygame.K_LEFT]:
            dx = -5
            self.direction = -1
        elif keys[pygame.K_RIGHT]:
            dx = 5
            self.direction = 1

        # Springen
        if not self.jumping and keys[pygame.K_SPACE]:
            self.vel_y = -12
            self.jumping = True

        # Zwaartekracht
        self.vel_y += 0.5
        if self.vel_y > 10:
            self.vel_y = 10
        dy = self.vel_y

        # Op de grond blijven
        if self.rect.bottom + dy > HEIGHT - 50:
            dy = HEIGHT - 50 - self.rect.bottom
            self.jumping = False

        # Beweging toepassen
        self.rect.x += dx
        self.rect.y += dy

        # Afbeelding aanpassen aan richting
        if self.direction == 1:
            self.image = self.image_right
        else:
            self.image = self.image_left

# Maak Mario
player = Mario(100, HEIGHT - 150)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Main loop
run = True
while run:
    clock.tick(FPS)
    
    screen.blit(bg, (0,-330))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
sys.exit()
