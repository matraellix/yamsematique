import pygame
import probas
import functions
# from menu import draw_text

pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('CaviarDreams.ttf', 18)
selected_category = [False, False, False, False, False,
                     False, False, False, False, False, False, False]
done = [False, False, False, False, False,
        False, False, False, False, False, False, False]
scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totals = [0, 0, 0, 0]
opponent_scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
opponent_totals = [0, 0, 0, 0]


class Category:
    def __init__(self, x_pos, y_pos, text, select, done, score):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.select = select
        self.done = done
        self.score = score

    def draw(self):
        pygame.draw.line(screen, (255, 245, 238), (self.x_pos,
                         self.y_pos), (self.x_pos + 224, self.y_pos), 1)

        if not self.done:
            functions.draw_text(self.text, font, (255, 245, 238),
                                screen, self.x_pos + 7, self.y_pos + 7)
        else:
            functions.draw_text(self.text, font, (100, 50, 50),
                                screen, self.x_pos + 6, self.y_pos + 6)
        if self.select:
            pygame.draw.rect(screen, ("#33211D"), [
                             self.x_pos, self.y_pos, 190, 30])
        functions.draw_text(self.text, font, (255, 245, 238),
                            screen, self.x_pos + 7, self.y_pos + 7)
        functions.draw_text(str(self.score), font, ("#33211D"),
                            screen, self.x_pos + 198, self.y_pos + 5)
    # def draw_select(self):


def make_choice(clicked_num, selected, done_list):
    for i in range(len(selected)):
        selected[i] = False
    if not done_list[clicked_num]:
        selected[clicked_num] = True
    return selected


def draw_categories(categories_array):
    for category in range(len(categories_array)):
        categories_array[category].draw()


def create_categories(dice_values):

    for i in range(0, 6):
        pygame.draw.rect(screen, (214, 125, 122), [50, 260 + i*35, 225, 30])

    for i in range(0, 6):
        pygame.draw.rect(screen, (255, 245, 238), [240, 260 + i*35, 35, 30])

    for i in range(0, 6):
        pygame.draw.rect(screen, (214, 125, 122), [300, 260 + i*35, 225, 30])

    for i in range(0, 6):
        pygame.draw.rect(screen, (255, 245, 238), [490, 260 + i*35, 35, 30])

    Category1 = Category(
        50, 260, "1", selected_category[0], done[0], scores[0])
    Category2 = Category(
        50, 295, "2", selected_category[1], done[1], scores[1])
    Category3 = Category(
        50, 330, "3", selected_category[2], done[2], scores[2])
    Category4 = Category(
        50, 365, "4", selected_category[3], done[3], scores[3])
    Category5 = Category(
        50, 400, "5", selected_category[4], done[4], scores[4])
    Category6 = Category(
        50, 435, "6", selected_category[5], done[5], scores[5])

    Small_straight = Category(
        300, 260, "Small Straight", selected_category[6], done[6], scores[6])
    Large_straight = Category(
        300, 295, "Large Straight", selected_category[7], done[7], scores[7])
    Brelan = Category(300, 330, "Brelan",
                      selected_category[8], done[8], scores[8])
    Full = Category(300, 365, "Full", selected_category[9], done[9], scores[9])
    Square = Category(300, 400, "Square",
                      selected_category[10], done[10], scores[10])
    Yams = Category(300, 435, "Yams",
                    selected_category[11], done[11], scores[11])

    Numbers_total = Category(50, 505, "Numbers total",
                             False, True, totals[0])
    Combinations_total = Category(
        300, 505, "Combination total", False, True, totals[1])

    Bonus_numbers = Category(50, 540, "Numbers bonus",
                             False, True, totals[2])
    total = totals[3]

    # done = check_done(done, dice_values)

    categories_numbers = [Category1, Category2, Category3,
                          Category4, Category5, Category6]
    draw_categories(categories_numbers)

    categories_combination = [Small_straight, Large_straight, Brelan,
                              Full, Square, Yams]
    draw_categories(categories_combination)

    categories_totals = [Numbers_total, Combinations_total, Bonus_numbers]

    draw_categories(categories_totals)

    pygame.draw.line(screen, (51, 33, 29), (50, 480), (525, 480), 1)

    return done, selected_category, scores


# PROBABLEMENT A DEPLACER DANS LE FICHIER OPPONENT


def create_categories_opponent():
    opponent_text = font.render(
        'Your Opponent: IAm', True, (255, 245, 238))
    screen.blit(opponent_text, (650, 15))

    for i in range(0, 12):
        pygame.draw.rect(screen, (214, 125, 122), [700, 50 + i*35, 225, 30])

    for i in range(0, 12):
        pygame.draw.rect(screen, (255, 245, 238), [890, 50 + i*35, 35, 30])

    Category1 = Category(700, 50, "1", False, False, opponent_scores[0])
    Category2 = Category(700, 85, "2", False, False, opponent_scores[0])
    Category3 = Category(700, 120, "3", False, False, opponent_scores[0])
    Category4 = Category(700, 155, "4", False, False, opponent_scores[0])
    Category5 = Category(700, 190, "5", False, False, opponent_scores[0])
    Category6 = Category(700, 225, "6", False, False, opponent_scores[0])

    Small_straight = Category(
        700, 260, "Small Straight", False, False, opponent_scores[0])
    Large_straight = Category(
        700, 295, "Large Straight", False, False, opponent_scores[0])
    Brelan = Category(700, 330, "Brelan", False, False, opponent_scores[0])
    Full = Category(700, 365, "Full", False, False, opponent_scores[0])
    Square = Category(700, 400, "Square", False, False, opponent_scores[0])
    Yams = Category(700, 435, "Yams", False, False, opponent_scores[0])

    Bonus_numbers = Category(700, 470, "Numbers bonus",
                             False, False, opponent_totals[0])

    Numbers_total = Category(700, 505, "Numbers total",
                             False, False, opponent_totals[1])
    Combinations_total = Category(
        700, 540, "Combination total", False, False, opponent_totals[2])

    # total = Bonus_numbers + Numbers_total + Combinations_total

    categories = [Category1, Category2, Category3,
                  Category4, Category5, Category6, Small_straight, Large_straight, Brelan,
                  Full, Square, Yams, Numbers_total, Combinations_total, Bonus_numbers]
    draw_categories(categories)

    # pygame.draw.line(screen, (51, 33, 29), (50, 480), (525, 480), 1)
