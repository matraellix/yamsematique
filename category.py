import pygame
import probas
import functions
# from menu import draw_text

pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('CaviarDreams.ttf', 18)


class Category:
    def __init__(self, x_pos, y_pos, text, select, done):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.select = select
        self.done = done

    def draw(self):
        pygame.draw.line(screen, (51, 33, 29), (self.x_pos,
                         self.y_pos), (self.x_pos + 225, self.y_pos), 2)

        if not self.done:
            functions.draw_text(self.text, font, (255, 245, 238),
                                screen, self.x_pos + 7, self.y_pos + 6)
        else:
            functions.draw_text(self.text, font, (214, 125, 122),
                                screen, self.x_pos + 7, self.y_pos + 6)


def draw_categories(categories_array):
    for category in range(len(categories_array)):
        categories_array[category].draw()


def create_categories():
    Category1 = Category(50, 260, "1", False, False)
    Category2 = Category(50, 290, "2", False, False)
    Category3 = Category(50, 320, "3", False, False)
    Category4 = Category(50, 350, "4", False, False)
    Category5 = Category(50, 380, "5", False, False)
    Category6 = Category(50, 410, "6", False, False)

    Small_straight = Category(300, 260, "Small Straight", False, False)
    Large_straight = Category(300, 290, "Large Straight", False, False)
    Brelan = Category(300, 320, "Brelan", False, False)
    Full = Category(300, 350, "Full", False, False)
    Square = Category(300, 380, "Square", False, False)
    Yams = Category(300, 410, "Yams", False, False)

    Numbers_total = Category(50, 500, "Numbers total", False, False)
    Combinations_total = Category(300, 500, "Combination total", False, False)

    Bonus_numbers = Category(50, 530, "Numbers bonus", False, False)
    total = 0

    categories_numbers = [Category1, Category2, Category3,
                          Category4, Category5, Category6]
    draw_categories(categories_numbers)

    categories_combination = [Small_straight, Large_straight, Brelan,
                              Full, Square, Yams]
    draw_categories(categories_combination)

    categories_totals = [Numbers_total, Combinations_total, Bonus_numbers]

    draw_categories(categories_totals)

    pygame.draw.line(screen, (51, 33, 29), (50, 450), (525, 450), 2)
