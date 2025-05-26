import pygame, json
class Blocks():

    def __init__(self) -> None:
        "Create Wall object"
        with open("trappen.json", "r") as fp:
            blokposities = json.load(fp)
        self.img = pygame.image.load(r"images/blokje.png")
        self.img  = pygame.transform.scale(self.img, (30,30)) 
        self.blokken: list[pygame.Rect] = []
        for blok in blokposities:
            self.blokken.append(pygame.Rect(blok[0],blok[1], self.img.get_width(), self.img.get_height()))

    def draw(self, screen:pygame.surface.Surface) -> None:
        "Draw wall on screen"

        # Overloop ieder blok & teken op scherm.
        for blok in self.blokken:
            screen.blit(self.img, (blok.x, blok.y))

        # Toon scherm aan gebruiker.
        pygame.display.flip()

