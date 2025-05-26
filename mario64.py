import pygame
from pygame.locals import *
from pygame import mixer
import random
import json


pygame.init()
mixer.init()

#fps
clock = pygame.time.Clock()
fps = 60 

#achtergrond
#bg = pygame.image.load('pyg/bg1.png') 

# Maak frame aan met bepaalde grootte.
breed = 800  
hoog = 600

frame = pygame.display.set_mode((breed, hoog))
pygame.display.set_caption('mario 69')

running = True
while running: 
    ##
    
pygame.quit() 

