import pygame
import sys
import terrein
from mario import Mario
import koepa


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


# Maak sprites
player = Mario(100, HEIGHT - 150)
enemy = koepa.KoepaTroepa(100, HEIGHT - 150)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)


# Main loop
run = True
while run:
    clock.tick(FPS)
    
    screen.blit(bg, (0,-330))
    keys = pygame.key.get_pressed()

    all_sprites.update(keys)
    all_sprites.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
sys.exit()
