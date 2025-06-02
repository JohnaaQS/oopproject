import pygame
import terrein, koepa
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
        self.direction = 1  # 1 = rechts, -1 = links
        
    def update(self, keys):
        dx = 0

        if keys[pygame.K_LEFT]:
            dx = -5
            self.direction = -1
        elif keys[pygame.K_RIGHT]:
            dx = 5
            self.direction = 1

        if not self.jumping and keys[pygame.K_SPACE]:
            self.vel_y = -12
            self.jumping = True

        self.vel_y += 0.5
        if self.vel_y > 10:
            self.vel_y = 10
        dy = self.vel_y

        from main import HEIGHT  
        if self.rect.bottom + dy > HEIGHT - 50:
            dy = HEIGHT - 50 - self.rect.bottom
            self.jumping = False

        self.rect.x += dx
        self.rect.y += dy

        self.image = self.image_right if self.direction == 1 else self.image_left
