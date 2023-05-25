import pygame
import probas
import category
import dice
from random import randint

pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('CaviarDreams.ttf', 18)

l = len(category.selected_category)
markmat_normal = [[1/l for i in range(l)] for j in range(l)]

markmats = [[], markmat_normal, []]


def median(set):
    copy = [v for v in set]
    copy.sort()
    return copy[len(copy)//2]


class Opponent:
    dice_values = [1, 2, 3, 4, 5, 6]

    def __init__(self, difficulty=0):
        self.total_score = 0
        self.difficulty = difficulty
        self.matrix = markmats[difficulty]
        self.pick_category = min
        if difficulty == 1:
            self.pick_category = median
        if difficulty == 2:
            self.pick_category = max
        self.done = [0 for i in range(len(category.selected_category))]

    def calculate_score(self):
        print(self.matrix)
        for i in range(len(category.selected_category)):
            dices = [randint(1, 6)]
            category_scores = []
            for i in range(5):
                dices.append(probas.markov(
                    Opponent.dice_values, dices[i], self.matrix))

            for i in range(len(category.selected_category)):
                category_scores.append(dice.check_scores(i, dices, self.done))

            self.total_score += self.pick_category(category_scores)
