import pygame
import probas
import category


pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('CaviarDreams.ttf', 18)


class Opponent:
    def __init__(self):
        self.total_score = 0
