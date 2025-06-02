import pygame
import sys
import terrein_GPT
from mario_GPT import Mario
import koepa


# Init
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Mannetje (1 afbeelding)")
blokke = terrein_GPT.Blocks()


# Clock
clock = pygame.time.Clock()
FPS = 60


# Kleuren
bg = pygame.image.load('images\Achtergrond.png')


# Maak sprites
player = Mario(100, HEIGHT - 150)
enemy = koepa.KoepaTroepa(300, HEIGHT - 150)

koepa_group = pygame.sprite.Group()
koepa_group.add(enemy)

mario_group = pygame.sprite.Group()
mario_group.add(player)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
# Main loop
run = True
while run:
    clock.tick(FPS)
    screen.blit(bg, (0,-330))
    keys = pygame.key.get_pressed()


    all_sprites.draw(screen)
    player.update(keys, blokke.blokken, HEIGHT)
    enemy.update()  # if your enemy needs updating

    blokke.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
sys.exit()
