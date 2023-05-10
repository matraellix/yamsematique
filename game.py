import pygame

WIDTH = 600
HEIGHT = 800
clicked = False
something_selected = False

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.window = pygame.display.set_mode([WIDTH, HEIGHT])
        self.caption = pygame.display.set_caption('Yamsematique!')
        self.timer = pygame.time.Clock()
        self.fps = 60
        self.font = font = pygame.font.Font('CaviarDreams.ttf', 18)
        self.roll = False
        self.scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.done = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.possible = [False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.game_over = False
        self.high_score = 0
        self.score = 0
        self.restart = ''

class Round():
    def __init__(self):
        self.rolls_left = 3
        self.diceSelected = [False, False, False, False, False]

