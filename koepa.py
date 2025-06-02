import pygame

class KoepaTroepa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_right = pygame.image.load('images/koopatroepa.png').convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right, (50, 60))
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.direction = 1
        self.speed = 2
        self.min_x = x - 100
        self.max_x = x + 100

    def update(self, *args):  # update methode
        self.rect.x += self.direction * self.speed

        if self.rect.left <= self.min_x:
            self.rect.left = self.min_x
            self.direction = 1
        elif self.rect.right >= self.max_x:
            self.rect.right = self.max_x
            self.direction = -1

        self.image = self.image_right if self.direction == 1 else self.image_left
