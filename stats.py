import pygame
import os
import dice
import random
import functions
import time
import dice
import category

pygame.init()

WIDTH = 500
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('CaviarDreams.ttf', 18)


def draw_stats():

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    timer = pygame.time.Clock()
    fps = 60
    running = True
    while running:
        timer.tick(fps)
        screen.fill((114, 47, 55))
        functions.draw_text('How many time did you roll :', font,
                            (255, 245, 238), screen, 20, 30)

        functions.draw_text('a 1 :', font,
                            (255, 245, 238), screen, 250, 30)
        functions.draw_text(str(dice.dicevalue_stats[0]), font,
                            (255, 245, 238), screen, 300, 30)

        functions.draw_text('a 2 :', font,
                            (255, 245, 238), screen, 250, 50)
        functions.draw_text(str(dice.dicevalue_stats[1]), font,
                            (255, 245, 238), screen, 300, 50)

        functions.draw_text('a 3 :', font,
                            (255, 245, 238), screen, 250, 70)
        functions.draw_text(str(dice.dicevalue_stats[2]), font,
                            (255, 245, 238), screen, 300, 70)

        functions.draw_text('a 4 :', font,
                            (255, 245, 238), screen, 250, 90)
        functions.draw_text(str(dice.dicevalue_stats[3]), font,
                            (255, 245, 238), screen, 300, 90)

        functions.draw_text('a 5 :', font,
                            (255, 245, 238), screen, 250, 110)
        functions.draw_text(str(dice.dicevalue_stats[4]), font,
                            (255, 245, 238), screen, 300, 110)

        functions.draw_text('a 6 :', font,
                            (255, 245, 238), screen, 250, 130)
        functions.draw_text(str(dice.dicevalue_stats[5]), font,
                            (255, 245, 238), screen, 300, 130)

        functions.draw_text('the number you rolled the most: ', font,
                            (255, 245, 238), screen, 20, 180)

        pygame.draw.rect(screen, (255, 255, 255), [
                         10, 220, 480, 70], 1, 20)
        functions.draw_text('your final score: ', font,
                            (255, 245, 238), screen, 20, 230)
        functions.draw_text(str(category.totals[3]), font,
                            (255, 245, 238), screen, 300, 230)
        functions.draw_text('your AI opponent\'s final score: ', font,
                            (255, 245, 238), screen, 20, 255)
        functions.draw_text("score of ai", font,
                            (255, 245, 238), screen, 300, 255)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()
    back_menu()


def back_menu():
    WIDTH_back_menu = 400
    HEIGHT_back_menu = 500
    screen = pygame.display.set_mode((WIDTH_back_menu, HEIGHT_back_menu))
