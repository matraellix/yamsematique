"""
Importing important libraries
"""
import pygame

pygame.init()
pygame.display.set_caption('Yamsématiques')

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
#setting font settings
font = pygame.font.Font('CaviarDreams.ttf', 18)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
# A variable to check for the status later
click = False
 
# Main container function that holds the buttons and game functions
def main_menu():
    running = True
    while running:
 
        screen.fill((114, 47, 55))
        draw_text('Menu', font, (255,245,238), screen, 280, 40)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_lvl1 = pygame.Rect(200, 100, 200, 50)
        button_lvl2 = pygame.Rect(200, 180, 200, 50)
        button_lvl3 = pygame.Rect(200, 260, 200, 50)
        button_quit = pygame.Rect(200, 340, 200, 50)

        #defining functions when a certain button is pressed
        if button_lvl1.collidepoint((mx, my)):
            if click:
                run_lvl("Choisissez un chiffre compris entre 1 et 6")
        if button_lvl2.collidepoint((mx, my)):
            if click:
                run_lvl2()
        if button_lvl3.collidepoint((mx, my)):
            if click:
                run_lvl("Choisissez un nombre positif")
        if button_quit.collidepoint((mx, my)):
            if click:
                running = False
        pygame.draw.rect(screen, (255,245,238), button_lvl1)
        pygame.draw.rect(screen, (255,245,238), button_lvl2)
        pygame.draw.rect(screen, (255,245,238), button_lvl3)
        pygame.draw.rect(screen, (255,245,238), button_quit)
 
        #writing text on top of button
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
def run_lvl2():
    proba = choose_proba("Choisissez une probabilité entre 0 et 1")
    print(proba)
    running = True
    while running:
        screen.fill((114, 47, 55))
        draw_text('proba : ' + proba, font, (255,245,238), screen, 140, 32)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

"""
NIVEAU 1 UNIFORME - 3 POISSON
"""
def run_lvl(instruction):
    proba = choose_proba(instruction)
    print(proba)
    running = True
    while running:
        screen.fill((114, 47, 55))
        draw_text('proba : ' + proba, font, (255,245,238), screen, 140, 32)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

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
        draw_text(instruction, font, (255,245,238), screen, 150, 200)
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
                    return proba_chosen[:-1]
        if active:
            color = color_active
        else:
            color = color_passive            
        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, color, input_proba)
        text_surface = font.render(proba_chosen, True, (255,245,238))
        # render at position stated in arguments
        screen.blit(text_surface, (input_proba.x+5, input_proba.y+5))
        # set width of textfield so that text cannot get outside of user's text input
        input_proba.w = max(100, text_surface.get_width()+10)
        
        pygame.display.update()

"""
END FUNCTIONS
""" 

main_menu()