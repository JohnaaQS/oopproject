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
# bg = pygame.transform.scale(bg, (bg.get_width(), HEIGHT)) 
# world_width = bg.get_width()  # Width of the full background world


# Maak sprites
player = Mario(100, HEIGHT - 150)
enemy = koepa.KoepaTroepa(300, HEIGHT - 120)

koepa_group = pygame.sprite.Group()
koepa_group.add(enemy)

mario_group = pygame.sprite.Group()
mario_group.add(player)

offset_x = 0

# Main loop
run = True
while run:
    clock.tick(FPS)
    screen.blit(bg, (0,-330))
    keys = pygame.key.get_pressed()

    mario_group.update(keys, koepa_group, HEIGHT)
    player = mario_group.sprites()[0]
    
    if player.dood:
        run = False  # Of toon een game over scherm
    
    mario_group.draw(screen)
    koepa_group.update()
    koepa_group.draw(screen)
    
    blokken.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
sys.exit()
