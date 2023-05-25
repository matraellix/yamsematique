import pygame
import probas
import category
import os
import dice
import random
import functions
import time

pygame.init()

WIDTH = 500
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('CaviarDreams.ttf', 19)


class Demoyams:
    def __init__(self, x_pos, y_pos, face_value):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.face_value = face_value

    def draw(self):

        pygame.draw.rect(screen, (255, 255, 255), [
                         self.x_pos, self.y_pos, 180, 180], 0, 5)
        font_dice = pygame.font.Font('CaviarDreams.ttf', 40)

        if self.face_value == 'demoyams':

            functions.draw_text('DEMO', font_dice,
                                '#731C10', screen, self.x_pos+35, self.y_pos+40)
            functions.draw_text('YAMS', font_dice,
                                '#731C10', screen, self.x_pos+40, self.y_pos+90)
        elif self.face_value == 'joker':
            functions.draw_text(self.face_value.upper(), font_dice,
                                '#65743A', screen, self.x_pos+30, self.y_pos+60)


def draw_demoyams():
    demoyams_value = ''
    demoyams_once = 1
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    timer = pygame.time.Clock()
    fps = 60
    roll_demoyams = False
    roll_left = 1
    running = True
    while running:
        timer.tick(fps)
        screen.fill((114, 47, 55))
        # BUTTON ROLL
        button_roll_demoyams = pygame.draw.rect(
            screen, (255, 245, 238), [50, 280, 230, 50])
        roll_demoyams_text = font.render(
            'ROLL THE DEMOYAMS', True, (60, 25, 29))
        screen.blit(roll_demoyams_text, (70, 295))
        # BUTTON SKIP
        button_skip = pygame.draw.rect(
            screen, (255, 245, 238), [350, 280, 100, 50])
        roll_demoyams_text = font.render('SKIP', True, (60, 25, 29))
        screen.blit(roll_demoyams_text, (380, 295))

        
        functions.draw_text('your current score : ' + str(category.totals[3]), font,
                            (255, 245, 238), screen, 100, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN and roll_left > 0:
                if button_roll_demoyams.collidepoint(event.pos):
                    roll_demoyams = True
                    roll_left = 0

        if roll_demoyams:
            faces = ['joker', 'demoyams']
            demoyams_value = random.choice(faces)
            roll_demoyams = False
            # running = False
        demoyams = Demoyams(170, 50, demoyams_value)
        if demoyams_value != '' and demoyams_once > 0:
            demoyams.draw()
            demoyams_once = 0
            score_to_change = category.scores[k := probas.uniformdisc(0, 12)]
            functions.draw_text('the score from the category that changed : ' + str(k+1), font,
                                (255, 245, 238), screen, 50, 430)

            # print(score_to_change)
            operation = probas.uniformdisc(0, 2)
            # print(str(operation)+' operation')
            if demoyams_value == 'joker':
                if operation == 0:
                    score_to_change += (z := probas.uniformdisc(1, 50))
                    # print(str(z)+' nb +')
                elif operation == 1:
                    score_to_change *= (w := probas.uniformdisc(1, 10))
                    # print(str(w)+' nb *')
            elif demoyams_value == 'demoyams':
                score_to_change = 0
            category.scores[k] = score_to_change
            final_total = dice.check_totals(
                category.totals, category.scores)[3]
            # print(final_total)
            functions.draw_text('your new full score : ' + str(final_total), font,
                                (255, 245, 238), screen, 100, 500)
            pygame.display.update()
            time.sleep(4)
            running = False
        pygame.display.update()


def back_menu():
    WIDTH_back_menu = 400
    HEIGHT_back_menu = 500
    screen = pygame.display.set_mode((WIDTH_back_menu, HEIGHT_back_menu))
