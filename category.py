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
    Category1 = Category(50, 300, "1", False, False)
    Category2 = Category(50, 330, "2", False, False)
    Category3 = Category(50, 360, "3", False, False)
    Category4 = Category(50, 390, "4", False, False)
    Category5 = Category(50, 420, "5", False, False)
    Category6 = Category(50, 450, "6", False, False)

    Small_straight = Category(300, 300, "Small Straight", False, False)
    Large_straight = Category(300, 330, "Large Straight", False, False)
    Brelan = Category(300, 360, "Brelan", False, False)
    Full = Category(300, 390, "Full", False, False)
    Square = Category(300, 420, "Square", False, False)
    Yams = Category(300, 450, "Yams", False, False)

    categories_numbers = [Category1, Category2, Category3,
                          Category4, Category5, Category6]
    draw_categories(categories_numbers)

    categories_combination = [Small_straight, Large_straight, Brelan,
                              Full, Square, Yams]
    draw_categories(categories_combination)

    pygame.draw.line(screen, (51, 33, 29), (50, 480), (525, 480), 2)
