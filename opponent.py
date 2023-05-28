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

l = 6

markmat_difficult = [[1/8, 1/8, 1/8, 1/8, 1/4, 1/4] for i in range(l)]

markmat_normal = [[1/l for i in range(l)] for j in range(l)]

markmat_easy = [[1/l for i in range(l)]]
for i in range(l-1):
    markmat_easy.append([1,0,0,0,0,0])

markmats = [markmat_easy, markmat_normal, markmat_difficult]

score_ai = 0

def median(set):
    copy = [v for v in set]
    copy.sort()
    return copy[len(copy)//2]

def minpos(set) :
    posset = [v for v in set if v>0]
    if len(posset) :
        return min(posset)
    return 0

class Opponent:
    dice_values = [1, 2, 3, 4, 5, 6]

    def __init__(self, difficulty=0):
        self.total_score = 0
        self.difficulty = difficulty
        self.matrix = markmats[difficulty]
        self.pick_category = minpos
        if difficulty == 1:
            self.pick_category = median
        if difficulty == 2:
            self.pick_category = max
        self.done = [0 for i in range(len(category.selected_category))]

    def calculate_score(self):
        global score_ai
        score_ai = 0
        for i in range(len(category.selected_category)):
            dices = [randint(1, 6)]
            category_scores = []
            for i in range(4):
                dices.append(probas.markov(
                    Opponent.dice_values, dices[i]-1, self.matrix))

            category.selected_category = [0 for i in range(12)]
            for i in range(len(category.selected_category)):
                category.selected_category[i] = 1
                category_scores.append(dice.check_scores(category.selected_category, dices, self.done))
                category.selected_category[i] = 0

            score = self.pick_category(category_scores)
            self.total_score += score
            self.done[category_scores.index(score)] = 1
            score_ai = self.total_score



