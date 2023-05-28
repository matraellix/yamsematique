"""
Importing important libraries
"""
import pygame
import probas
import dice
import functions
import opponent
import os
import demoyams
import stats


pygame.init()
pygame.display.set_caption('Yamsématiques')

WIDTH = 400
HEIGHT = 500
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

level = 1

# setting font settings
font = pygame.font.Font('CaviarDreams.ttf', 18)

# A variable to check for the status later
click = False
level_proba = 0.0

# Main container function that holds the buttons and game functions


def main_menu():
    running = True
    global click
    global level
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    while running:

        screen.fill((114, 47, 55))
        functions.draw_text('Menu', font, (255, 245, 238), screen, 180, 40)
        # Two variables to keep the position of the mouse
        mx, my = pygame.mouse.get_pos()
        # creating buttons
        button_lvl1 = pygame.Rect(100, 100, 200, 50)
        button_lvl2 = pygame.Rect(100, 180, 200, 50)
        button_lvl3 = pygame.Rect(100, 260, 200, 50)
        button_quit = pygame.Rect(100, 340, 200, 50)

        # defining functions when a certain button is pressed
        if button_lvl1.collidepoint((mx, my)):
            if click:
                click = False
                choose_law = probas.uniformdisc(0,1)
                if choose_law == 0:
                    law_lvl1 = 'normal'
                    probas_bonus = display_bonus_lvl1(law_lvl1, click)
                    bonus_law = probas.normal(probas_bonus[0], probas_bonus[1])
                else:
                    law_lvl1 = 'laplace'
                    probas_bonus = display_bonus_lvl1(law_lvl1, click)
                    bonus_law = probas.laplace(probas_bonus[0], probas_bonus[1])
                
                dice.Dice.pick = probas.uniformdisc
                dice.Dice.pick_params = [1, 6]
                dice.main_draw(bonus_law)
                #oppo = opponent.Opponent(level-1)
                #oppo.calculate_score()
                # Affichage des scores
                demoyams.draw_demoyams()
                stats.draw_stats()

        if button_lvl2.collidepoint((mx, my)):
            if click:
                click = False
                level = 2
                level_proba = run_lvl(
                    "Choose a probability between 0 and 1", "Choose a positive number (0 excluded)", click)
                dice.Dice.pick = probas.binomdice
                dice.Dice.pick_params = [level_proba[0]]

                bonus_law = probas.expo(level_proba[1])
                dice.main_draw(bonus_law)
                #oppo = opponent.Opponent(level-1)
                #oppo.calculate_score()
                # Affichage des scores
                demoyams.draw_demoyams()
                stats.draw_stats()
        if button_lvl3.collidepoint((mx, my)):
            if click:
                click = False
                level = 3
                level_proba = run_lvl(
                    "Choose a number between 1 and 6", "Choose a positive number (0 excluded)", click)
                dice.Dice.pick = probas.poissondice
                dice.Dice.pick_params = [level_proba[0]]
                
                bonus_law = probas.gamma(level_proba[1])
                dice.main_draw(bonus_law)
                #oppo = opponent.Opponent(level-1)
                #oppo.calculate_score()
                # Affichage des scores
                demoyams.draw_demoyams()
                stats.draw_stats()
        if button_quit.collidepoint((mx, my)):
            if click:
                running = False

        pygame.draw.rect(screen, (255, 245, 238), button_lvl1)
        pygame.draw.rect(screen, (255, 245, 238), button_lvl2)
        pygame.draw.rect(screen, (255, 245, 238), button_lvl3)
        pygame.draw.rect(screen, (255, 245, 238), button_quit)

        # writing text on top of button
        functions.draw_text('LEVEL 1', font, (60, 25, 29), screen, 170, 115)
        functions.draw_text('LEVEL 2', font, (60, 25, 29), screen, 170, 195)
        functions.draw_text('LEVEL 3', font, (60, 25, 29), screen, 170, 275)
        functions.draw_text('QUIT', font, (60, 25, 29), screen, 170, 355)

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

def bonus_lvl1(law_name):
    input_p1 = pygame.Rect(155, 250, 140, 32)
    input_p2 = pygame.Rect(155, 150, 140, 32)
    p1_chosen = ''
    p2_chosen = ''
    p1_active = False
    p2_active = False

    p1_color_active = pygame.Color((60, 25, 29))
    p1_color_passive = pygame.Color('white')
    p1_color = p1_color_passive

    p2_color_active = pygame.Color((60, 25, 29))
    p2_color_passive = pygame.Color('white')
    p2_color = p2_color_passive

    running = True
    while running:
        screen.fill((114, 47, 55))
        functions.draw_text('In this level bonus/malus will be triggered from', font,(255, 245, 238), screen, 10, 32)
        functions.draw_text('time to time, following a law ' + str(law_name), font,(255, 245, 238), screen, 10, 55)

        functions.draw_text('Choose a real number', font,(255, 245, 238), screen, 110, 120)
        functions.draw_text('Choose a positive number (0 excluded)', font,(255, 245, 238), screen, 40, 220)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_p1.collidepoint(event.pos):

                    p1_active = True
                elif input_p2.collidepoint(event.pos):
                    p2_active = True
                else:
                    p1_active = False
                    p2_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and p1_active:
                    p1_chosen = p1_chosen[:-1]
                elif event.key == pygame.K_BACKSPACE and p2_active: 
                    p2_chosen = p2_chosen[:-1]
                    
                elif (event.key != pygame.K_KP_ENTER or event.key != pygame.K_RETURN) and p1_active:
                    p1_chosen += event.unicode
                    
                elif (event.key != pygame.K_KP_ENTER or event.key != pygame.K_RETURN) and p2_active:
                    p2_chosen += event.unicode
                    
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    p1 = float(p1_chosen)
                    p2 = float(p2_chosen)
                    return p1, p2
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if p1_active:
            p1_color = p1_color_active
            text_surface = font.render(p1_chosen, True, (255, 245, 238))
        else:
            p1_color = p1_color_passive
            text_surface = font.render(p1_chosen, True, (0, 0, 0))
                
        if p2_active:
            p2_color = p2_color_active
            text_surface_b = font.render(p2_chosen, True, (255, 245, 238))
        else:
            p2_color = p2_color_passive
            text_surface_b = font.render(p2_chosen, True, (0, 0, 0))


        pygame.draw.rect(screen, p1_color, input_p1)
        screen.blit(text_surface, (input_p1.x+5, input_p1.y+5))
        input_p1.w = max(100, text_surface.get_width()+10)

        pygame.draw.rect(screen, p2_color, input_p2)
        screen.blit(text_surface_b, (input_p2.x+5, input_p2.y+5))
        input_p2.w = max(100, text_surface_b.get_width()+10)

        pygame.display.update()

def display_bonus_lvl1(law_name, click):
    probas = bonus_lvl1(law_name)
    running = True
    while running:
        screen.fill((114, 47, 55))
        functions.draw_text('proba: ' + str(probas[0]), font,
                            (255, 245, 238), screen, 140, 32)
        functions.draw_text('value used to trigger bonus/malus event: ' + str(probas[1]), font,
                            (255, 245, 238), screen, 20, 80)

        # Two variables to keep the position of the mouse
        mx, my = pygame.mouse.get_pos()
        # starting button // little fonction later ?
        button_start = pygame.Rect(100, 115, 200, 50)
        pygame.draw.rect(screen, (255, 245, 238), button_start)
        functions.draw_text('START GAME', font, (60, 25, 29), screen, 155, 130)

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
    return probas

"""
LEVEL CHOICE
"""
def run_lvl(instruction, bonus_ins, click):
    probas = choose_proba(instruction, bonus_ins)
    running = True
    while running:
        screen.fill((114, 47, 55))
        functions.draw_text('proba: ' + str(probas[0]), font,
                            (255, 245, 238), screen, 140, 32)
        functions.draw_text('value used to trigger bonus/malus event: ' + str(probas[1]), font,
                            (255, 245, 238), screen, 20, 80)

        # Two variables to keep the position of the mouse
        mx, my = pygame.mouse.get_pos()
        # starting button // little fonction later ?
        button_start = pygame.Rect(100, 115, 200, 50)
        pygame.draw.rect(screen, (255, 245, 238), button_start)
        functions.draw_text('START GAME', font, (60, 25, 29), screen, 155, 130)

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
    return probas


"""
Function for the user to choose the probability wanted
"""


def choose_proba(instruction, bonus_ins):
    input_proba = pygame.Rect(155, 250, 140, 32)
    input_pbonus = pygame.Rect(155, 150, 140, 32)
    proba_chosen = ''
    pbonus_chosen = ''

    proba_color_active = pygame.Color((60, 25, 29))
    proba_color_passive = pygame.Color('white')
    proba_color = proba_color_passive

    bonus_color_active = pygame.Color((60, 25, 29))
    bonus_color_passive = pygame.Color('white')
    bonus_color = bonus_color_passive

    proba_active = False
    bonus_active = False
    global level
    print(level)

    running = True

    while running:
        screen.fill((114, 47, 55))
        functions.draw_text(instruction, font,
                            (255, 245, 238), screen, 50, 200)
        functions.draw_text(bonus_ins, font,
                            (255, 245, 238), screen, 50, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_proba.collidepoint(event.pos):
                    proba_active = True
                elif input_pbonus.collidepoint(event.pos):
                    bonus_active = True
                else:
                    proba_active = False
                    bonus_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and proba_active:
                    proba_chosen = proba_chosen[:-1]
                elif event.key == pygame.K_BACKSPACE and bonus_active: 
                    pbonus_chosen = pbonus_chosen[:-1]
                    
                elif (event.key != pygame.K_KP_ENTER or event.key != pygame.K_RETURN) and proba_active:
                    proba_chosen += event.unicode
                    
                elif (event.key != pygame.K_KP_ENTER or event.key != pygame.K_RETURN) and bonus_active:
                    pbonus_chosen += event.unicode
                    
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if level == 2:
                        try:
                            proba = float(proba_chosen)
                            bonus = float(pbonus_chosen)
                            if 0 <= proba <= 1:
                                return proba, bonus
                            else:
                                msg = "The probability must be bewteen 0 and 1"
                                print(msg)
                                functions.draw_text(msg, font, (255, 245, 238),
                                                    screen, 50, 200)
                                proba_chosen = ''
                        except ValueError:
                            errorMsg = "Error : The probability must be bewteen 0 and 1"
                            print(errorMsg)
                            functions.draw_text(errorMsg, font, (255, 245, 238),
                                                screen, 50, 200)
                            proba_chosen = ''
                    elif level == 3:
                        try:
                            proba = float(proba_chosen)
                            bonus = float(pbonus_chosen)
                            if 0 < proba <= 6:
                                return proba, bonus
                            else:
                                msg = "The number must be between 1 and 6"
                                print(msg)
                                functions.draw_text(msg, font, (255, 245, 238),
                                                    screen, 50, 200)
                                proba_chosen = ''
                        except ValueError:
                            errorMsg = "Error : The number must be between 1 and 6"
                            print(errorMsg)
                            functions.draw_text(errorMsg, font, (255, 245, 238),
                                                screen, 50, 200)
                            proba_chosen = ''
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if proba_active:
            proba_color = proba_color_active
            text_surface = font.render(proba_chosen, True, (255, 245, 238))
        else:
            proba_color = proba_color_passive
            text_surface = font.render(proba_chosen, True, (0, 0, 0))
        
        if bonus_active:
            bonus_color = bonus_color_active
            text_surface_b = font.render(pbonus_chosen, True, (255, 245, 238))
        else:
            bonus_color = bonus_color_passive
            text_surface_b = font.render(pbonus_chosen, True, (0, 0, 0))


        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, proba_color, input_proba)
        # render at position stated in arguments
        screen.blit(text_surface, (input_proba.x+5, input_proba.y+5))
        # set width of textfield so that text cannot get outside of user's text input
        input_proba.w = max(100, text_surface.get_width()+10)

        pygame.draw.rect(screen, bonus_color, input_pbonus)
        # render at position stated in arguments
        screen.blit(text_surface_b, (input_pbonus.x+5, input_pbonus.y+5))
        # set width of textfield so that text cannot get outside of user's text input
        input_pbonus.w = max(100, text_surface_b.get_width()+10)

        pygame.display.update()


"""
END FUNCTIONS
"""

main_menu()

pygame.quit()
