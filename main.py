import pygame
from pygame import *
import sys


# Screen  Sizes
WIDTH = 1080
HEIGHT = 720

game_title = "Jesse and Kumba chess game"


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(game_title)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



        
pygame.init()   