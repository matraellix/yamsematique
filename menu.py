"""
Importing important libraries
"""
import pygame
import probas

pygame.init()
pygame.display.set_caption('Yamsématiques')

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# setting font settings
font = pygame.font.Font('CaviarDreams.ttf', 18)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# A variable to check for the status later
click = False
level_proba = 0.0
selected = [False, False, False, False, False]

# Dice class


class Dice:
    def __init__(self, x_pos, y_pos, num, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num
        global selected
        self.key = key
        self.active = selected[self.key]
        self.dice = ''

    def draw(self):
        self.dice = pygame.draw.rect(screen, (255, 255, 255), [
            self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.number == 1:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number == 2:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 3:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 4:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 5:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 6:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.x_pos + 80, self.y_pos + 20), 10)
        if self.active:
            pygame.draw.rect(screen, (255, 0, 0), [
                             self.x_pos, self.y_pos, 100, 100], 4, 5)

    def check_click(self, coordinates):
        if self.dice.collidepoint(coordinates):
            if selected[self.key]:
                selected[self.key] = False
            elif not selected[self.key]:
                selected[self.key] = True

# Main container function that holds the buttons and game functions


def main_menu():
    running = True
    global click

    while running:

        screen.fill((114, 47, 55))
        draw_text('Menu', font, (255, 245, 238), screen, 280, 40)
        # Two variables to keep the position of the mouse
        mx, my = pygame.mouse.get_pos()
        # creating buttons
        button_lvl1 = pygame.Rect(200, 100, 200, 50)
        button_lvl2 = pygame.Rect(200, 180, 200, 50)
        button_lvl3 = pygame.Rect(200, 260, 200, 50)
        button_quit = pygame.Rect(200, 340, 200, 50)

        # defining functions when a certain button is pressed
        if button_lvl1.collidepoint((mx, my)):
            if click:
                click = False
                level_proba = run_lvl(
                    "Choisissez un chiffre compris entre 1 et 6")

        if button_lvl2.collidepoint((mx, my)):
            if click:
                click = False
                level_proba = run_lvl2(click)
                main_game(level_proba, click)

        if button_lvl3.collidepoint((mx, my)):
            if click:
                level_proba = run_lvl("Choisissez un nombre positif")
        if button_quit.collidepoint((mx, my)):
            if click:
                running = False
        pygame.draw.rect(screen, (255, 245, 238), button_lvl1)
        pygame.draw.rect(screen, (255, 245, 238), button_lvl2)
        pygame.draw.rect(screen, (255, 245, 238), button_lvl3)
        pygame.draw.rect(screen, (255, 245, 238), button_quit)

        # writing text on top of button
        draw_text('NIVEAU 1', font, (60, 25, 29), screen, 270, 115)
        draw_text('NIVEAU 2', font, (60, 25, 29), screen, 270, 195)
        draw_text('NIVEAU 3', font, (60, 25, 29), screen, 270, 275)
        draw_text('QUITTER', font, (60, 25, 29), screen, 270, 355)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


"""
NIVEAU 2 - BINOMIALE
"""


def run_lvl2(click):
    proba = choose_proba("Choisissez une probabilité entre 0 et 1")
    print(proba)
    running = True
    while running:
        screen.fill((114, 47, 55))
        draw_text('proba : ' + proba, font, (255, 245, 238), screen, 140, 32)

        # Two variables to keep the position of the mouse
        mx, my = pygame.mouse.get_pos()
        # starting button // little fonction later ?
        button_start = pygame.Rect(200, 100, 200, 50)
        pygame.draw.rect(screen, (255, 245, 238), button_start)
        draw_text('START GAME', font, (60, 25, 29), screen, 250, 115)

        if button_start.collidepoint((mx, my)):
            if click:
                running = False

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

    return proba


"""
NIVEAU 1 UNIFORME - 3 POISSON
"""


def run_lvl(instruction):
    proba = choose_proba(instruction)
    print(proba)
    running = True
    while running:
        screen.fill((114, 47, 55))
        draw_text('proba : ' + proba, font, (255, 245, 238), screen, 140, 32)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    return proba


"""
Function for the user to choose the probability wanted
"""


def choose_proba(instruction):
    input_proba = pygame.Rect(250, 250, 140, 32)
    proba_chosen = ''

    color_active = pygame.Color((60, 25, 29))
    color_passive = pygame.Color('white')
    color = color_passive
    active = False

    running = True

    while running:
        screen.fill((114, 47, 55))
        draw_text(instruction, font, (255, 245, 238), screen, 150, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_proba.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    proba_chosen = proba_chosen[:-1]
                else:
                    proba_chosen += event.unicode
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:

                    try:
                        proba = float(proba_chosen)
                        if 0 <= proba <= 1:
                            return proba_chosen[:-1]
                        else:
                            msg = "La probabilité doit être entre 0 et 1."
                            print(msg)
                            draw_text(msg, font, (255, 245, 238),
                                      screen, 150, 200)
                            proba_chosen = ''
                    except ValueError:
                        errorMsg = "Erreur : Veuillez entrer un nombre valide entre 0 et 1."
                        print(errorMsg)
                        draw_text(errorMsg, font, (255, 245, 238),
                                  screen, 150, 200)
                        proba_chosen = ''
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if active:
            color = color_active
        else:
            color = color_passive
        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, color, input_proba)
        text_surface = font.render(proba_chosen, True, (255, 245, 238))
        # render at position stated in arguments
        screen.blit(text_surface, (input_proba.x+5, input_proba.y+5))
        # set width of textfield so that text cannot get outside of user's text input
        input_proba.w = max(100, text_surface.get_width()+10)

        pygame.display.update()


# def main_game(level_proba,click, bonusTimeVar):
def main_game(level_proba, click):
    timer = pygame.time.Clock()
    fps = 60
    running = True
    game_over = False
    roll = False
    rolls_left = 3
    selected = [False, False, False, False, False]
    scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    done = [False, False, False, False, False, False,
            False, False, False, False, False, False, False]

    while running and not game_over:
        timer.tick(fps)
        # screen.fill((114, 47, 55))
        numbers = [0, 0, 0, 0, 0]
        screen.fill((100, 20, 55))
        # Two variables to keep the position of the mouse
        mx, my = pygame.mouse.get_pos()
        # starting button // little fonction later ?
        button_roll = pygame.Rect(250, 185, 100, 50)
        pygame.draw.rect(screen, (255, 245, 238), button_roll)
        draw_text('ROLL', font, (60, 25, 29), screen, 280, 200)
        if roll:
            for number in range(len(numbers)):
                if not selected[number]:
                    numbers[number] = probas.uniformdisc(1, 6)
            roll = False

        dice1 = Dice(10, 50, numbers[0], 0)
        dice2 = Dice(130, 50, numbers[1], 1)
        dice3 = Dice(250, 50, numbers[2], 2)
        dice4 = Dice(370, 50, numbers[3], 3)
        dice5 = Dice(490, 50, numbers[4], 4)
        dice_array = [dice1, dice2, dice3, dice4, dice5]
        draw_dice(dice_array)

        draw_text(str(rolls_left), font,
                  (60, 25, 29), screen, 250, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_roll.collidepoint((mx, my)) and rolls_left > 0:
                    roll = True
                    rolls_left -= 1
                    draw_text(str(rolls_left), font,
                              (60, 25, 29), screen, 250, 250)
                    dice_clicked = 0

        pygame.display.update()


def draw_dice(dice_array):
    dice_array[0].draw()
    dice_array[1].draw()
    dice_array[2].draw()
    dice_array[3].draw()
    dice_array[4].draw()


"""
END FUNCTIONS
"""

main_menu()
