import os
import pygame
from random import randint

font_size = 30
speed_loop = 0.05

black = (0, 0, 0)
size = 15

width = 1260
heigth = 720

list_alf = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*"]

screen = pygame.display.set_mode((width, heigth), pygame.FULLSCREEN)
pygame.display.set_caption("MATRIX")

class Text:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.list_alf = list_alf

    def updade(self):
        self.y += 15
        if self.y >= heigth:
            self.y = randint(-1500, -500)
