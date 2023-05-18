import pygame
import probas
import category
import os


pygame.init()

WIDTH = 1000
HEIGHT = 650
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('CaviarDreams.ttf', 18)
clicked = -1
something_selected = False

current_scores = 0


class Dice:
    def __init__(self, x_pos, y_pos, num, key):
        global dice_selected
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num
        self.key = key
        self.die = ''
        self.selected = dice_selected[key]

    def draw(self):
        self.die = pygame.draw.rect(screen, (255, 255, 255), [
                                    self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.number == 1:
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number == 2:
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 3:
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 4:
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 5:
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 6:
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (51, 33, 29),
                               (self.x_pos + 80, self.y_pos + 20), 10)
        if self.selected:
            pygame.draw.rect(screen, (143, 201, 163), [
                self.x_pos, self.y_pos, 100, 100], 4, 5)

    def check_click(self, coordinates):
        if self.die.collidepoint(coordinates):
            if dice_selected[self.key]:
                dice_selected[self.key] = False
            elif not dice_selected[self.key]:
                dice_selected[self.key] = True


def check_scores(selected_category, dice_values, done, current_scores):
    active = 0
    max_count = 0
    for i in range(len(selected_category)):
        if selected_category[i]:
            active = i
    if active == 0 and not done[0]:
        current_scores = dice_values.count(1)
    elif active == 1 and not done[1]:
        current_scores = dice_values.count(2) * 2
    elif active == 2 and not done[2]:
        current_scores = dice_values.count(3) * 3
    elif active == 3 and not done[3]:
        current_scores = dice_values.count(4) * 4
    elif active == 4 and not done[4]:
        current_scores = dice_values.count(5) * 5
    elif active == 5 and not done[5]:
        current_scores = dice_values.count(6) * 6
    # brelan and square
    elif active == 8 and not done[8]:
        for j in range(1, 7):
            if dice_values.count(j) > max_count:
                max_count = dice_values.count(j)
        if max_count == 3:
            current_scores = sum(dice_values)
        else:

            current_scores = 0

    elif active == 10 and not done[10]:
        for j in range(1, 7):
            if dice_values.count(j) > max_count:
                max_count = dice_values.count(j)
        if max_count == 4:
            current_scores = 40 + sum(dice_values)
        else:
            current_scores = 0

    elif active == 9 and not done[9]:
        # Full
        for j in range(1, 7):
            if dice_values.count(j) > max_count:
                max_count = dice_values.count(j)
        if max_count == 3:
            for k in range(len(dice_values)):
                if dice_values.count(dice_values[k]) == 2:
                    current_scores = 30 + sum(dice_values)
        else:
            current_scores = 0
    elif active == 6 and not done[6]:
        lowest = 10
        highest = 0
        for l in range(len(dice_values)):
            if dice_values[l] < lowest:
                lowest = dice_values[l]
            if dice_values[l] > highest:
                highest = dice_values[l]
        if (lowest + 1 in dice_values) and (lowest + 2 in dice_values) and (lowest+3 in dice_values) and (lowest+4 in dice_values):
            current_scores = 40
        else:
            current_scores = 0

    elif active == 7 and not done[7]:

        lowest = 10
        highest = 0
        for l in range(len(dice_values)):
            if dice_values[l] < lowest:
                lowest = dice_values[l]
            if dice_values[l] > highest:
                highest = dice_values[l]
        if (highest - 1 in dice_values) and (highest - 2 in dice_values) and (highest - 3 in dice_values) and (highest - 4 in dice_values):
            current_scores = 45
        else:
            current_scores = 0
    elif active == 11 and not done[11]:
        for m in range(1, 7):
            if dice_values.count(m) > max_count:
                max_count = dice_values.count(m)
        if max_count == 5:
            # ou 100 si je fais comme les parents
            current_scores = 50 + sum(dice_values)
        else:
            current_scores = 0
    return current_scores


def draw_dices(dices_array):
    for die in range(len(dices_array)):
        dices_array[die].draw()


def main_draw():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    timer = pygame.time.Clock()
    fps = 60
    # if 0,0,0,0,0 it looks like a yams, so choose random values that don't follow each other
    global something_selected
    dice_values = [0, 7, 9, 11, 13]
    global dice_selected
    dice_selected = [False, False, False, False, False]
    roll = False
    rolls_left = 3
    running = True
    while running:
        timer.tick(fps)
        screen.fill((114, 47, 55))
        # BUTTON ROLL
        button_roll = pygame.draw.rect(
            screen, (255, 245, 238), [250, 185, 100, 50])
        roll_text = font.render('ROLL', True, (60, 25, 29))
        screen.blit(roll_text, (280, 200))

        # BUTTON ACCEPT
        button_accept = pygame.draw.rect(
            screen, (255, 245, 238), [380, 185, 145, 50])
        accept_text = font.render('ACCEPT TURN', True, (60, 25, 29))
        screen.blit(accept_text, (395, 200))

        # ROLLS LEFT TEXT
        turns_text = font.render(
            'Rolls Left This Turn: ' + str(rolls_left), True, (255, 245, 238))
        screen.blit(turns_text, (15, 15))
        # DICE
        dice1 = Dice(10, 50, dice_values[0], 0)
        dice2 = Dice(130, 50, dice_values[1], 1)
        dice3 = Dice(250, 50, dice_values[2], 2)
        dice4 = Dice(370, 50, dice_values[3], 3)
        dice5 = Dice(490, 50, dice_values[4], 4)
        dices_array = [dice1, dice2, dice3, dice4, dice5]

        draw_dices(dices_array)

        done, selected_category, scores = category.create_categories(
            dice_values)
        category.create_categories_opponent()
        current_scores = check_scores(
            selected_category, dice_values, done, scores)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for value in range(len(dices_array)):
                    dices_array[value].check_click(event.pos)

                if 50 <= event.pos[0] <= 225:
                    if 260 <= event.pos[1] <= 435:
                        if 260 <= event.pos[1] <= 295:
                            clicked = 0
                        if 295 <= event.pos[1] <= 330:
                            clicked = 1
                        if 330 <= event.pos[1] <= 365:
                            clicked = 2
                        if 365 <= event.pos[1] <= 400:
                            clicked = 3
                        if 400 <= event.pos[1] <= 435:
                            clicked = 4
                        if 435 <= event.pos[1] <= 470:
                            clicked = 5
                        print(clicked)
                        selected_category = category.make_choice(
                            clicked, selected_category, done)
                        clicked = -1
                elif 300 <= event.pos[0] <= 525:
                    if 260 <= event.pos[1] <= 435:
                        if 260 <= event.pos[1] <= 295:
                            clicked = 6
                        if 295 <= event.pos[1] <= 330:
                            clicked = 7
                        if 330 <= event.pos[1] <= 365:
                            clicked = 8
                        if 365 <= event.pos[1] <= 400:
                            clicked = 9
                        if 400 <= event.pos[1] <= 435:
                            clicked = 10
                        if 435 <= event.pos[1] <= 470:
                            clicked = 11
                        print(clicked)
                        selected_category = category.make_choice(
                            clicked, selected_category, done)
                        clicked = -1
                if button_roll.collidepoint(event.pos) and rolls_left > 0:
                    roll = True
                    rolls_left -= 1

                if button_accept.collidepoint(event.pos) and something_selected and rolls_left >= 0:
                    print("accepted")

                    for i in range(len(selected_category)):
                        if selected_category[i]:
                            done[i] = True
                            scores[i] = current_scores
                            print(selected_category[i])
                            print(i)
                            selected_category[i] = False

                    for j in range(len(dice_selected)):
                        dice_selected[j] = False
                    dice_values = [0, 7, 9, 11, 13]
                    something_selected = False
                    rolls_left = 3

        if roll:
            for value in range(len(dice_values)):
                if not dice_selected[value]:
                    dice_values[value] = probas.uniformdisc(1, 6)
            roll = False
        for i in range(len(done)):
            if selected_category[i]:
                something_selected = True

        pygame.display.flip()
    WIDTH_back_menu = 400
    HEIGHT_back_menu = 500
    screen = pygame.display.set_mode((WIDTH_back_menu, HEIGHT_back_menu))

# Uncomment for testing the file
# main_draw()
