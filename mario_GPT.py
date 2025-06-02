import pygame
import terrein_GPT, koepa

class Mario(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.image.load('images/mario.png').convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right, (50, 60))
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.vel_y = 0
        self.jumping = False
        self.direction = 1  # 1 = right, -1 = left

    def update(self, keys, blokken_groep, HEIGHT):
        dx = 0

        # Horizontal movement
        if keys[pygame.K_LEFT]:
            dx = -5
            self.direction = -1
        elif keys[pygame.K_RIGHT]:
            dx = 5
            self.direction = 1

        # Jumping
        if not self.jumping and keys[pygame.K_SPACE]:
            self.vel_y = -12
            self.jumping = True

        # Apply gravity
        self.vel_y += 0.5
        if self.vel_y > 10:
            self.vel_y = 10
        dy = self.vel_y

        # --- MOVE HORIZONTALLY AND CHECK COLLISIONS ---
        self.rect.x += dx
        collided_blocks = pygame.sprite.spritecollide(self, blokken_groep, False)
        for blok in collided_blocks:
            if dx > 0:  # moving right; collide with left side of block
                self.rect.right = blok.rect.left
            elif dx < 0:  # moving left; collide with right side of block
                self.rect.left = blok.rect.right

        # --- MOVE VERTICALLY AND CHECK COLLISIONS ---
        self.rect.y += dy
        collided_blocks = pygame.sprite.spritecollide(self, blokken_groep, False)
        for blok in collided_blocks:
            if dy > 0:  # falling down; collide with top of block
                self.rect.bottom = blok.rect.top
                self.vel_y = 0
                self.jumping = False
            elif dy < 0:  # jumping up; collide with bottom of block
                self.rect.top = blok.rect.bottom
                self.vel_y = 0

        # Prevent falling below ground level
        if self.rect.bottom > HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.vel_y = 0
            self.jumping = False

        # Set correct image based on direction
        self.image = self.image_right if self.direction == 1 else self.image_left