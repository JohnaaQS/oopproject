import pygame
import json

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

class Blocks:
    def __init__(self):
        # Load block positions from JSON file
        with open("trappen.json", "r") as fp:
            blokposities = json.load(fp)

        # Load and scale the block image once
        self.img = pygame.image.load(r"images\blokje.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (30, 30))

        # Create a sprite group to hold all block sprites
        self.blokken = pygame.sprite.Group()

        # Create a Block sprite for each position and add to the group
        for pos in blokposities:
            # Defensive check: pos should be a list or tuple with 2 values
            if isinstance(pos, (list, tuple)) and len(pos) == 2:
                blok_sprite = Block(pos[0], pos[1], self.img)
                self.blokken.add(blok_sprite)
            else:
                print(f"Warning: Invalid block position skipped: {pos}")

    def draw(self, screen: pygame.Surface):
        # Draw all blocks to the screen
        self.blokken.draw(screen)
