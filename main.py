import pygame
import button

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("yams")

#game variables
menu_started = False
menu_state = "main"

#define fonts
font = pygame.font.Font('CaviarDreams.ttf', 18)
#define colours
TEXT_COL = (255, 255, 255)

#load button
quit_img = pygame.image.load("button_back.png").convert_alpha()

#create button instances
level1_button = button.Button(220, 100, quit_img, 1)
level2_button = button.Button(220, 200, quit_img, 1)
level3_button = button.Button(220, 300, quit_img, 1)
quit_button = button.Button(220, 400, quit_img, 1)

input_box = pygame.Rect(100, 100, 140, 32)
user_text = ''


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def run_lvl1():
    draw_text("Choisissez une probabilité entre 0 et 1", font, TEXT_COL, 220, 250)

#game loop
run = True
while run:
    screen.fill((52, 78, 91))
    text_surface = font.render(user_text, True, (255,255,255))
    screen.blit(text_surface, (0,0))
    if menu_started == False:
        draw_text("Yam's press space to start", font, TEXT_COL, 220, 250)
    else:
        if menu_state == "main":
            if level1_button.draw(screen):
                menu_state = "lvl1"
            if level2_button.draw(screen):
                menu_state = "lvl2"
            if level3_button.draw(screen):
                menu_state = "lvl3"
            if quit_button.draw(screen):
                run = False
        if menu_state == "lvl1":
            run_lvl1()
        if menu_state == "lvl2":
            draw_text("Choose your probabilities", font, TEXT_COL, 220, 250)
        if menu_state == "lvl3":
            draw_text("Choose your probabilities", font, TEXT_COL, 220, 250)

    #event handler
    for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu_started = True
            if menu_state == "lvl1":
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else :
                    user_text += event.unicode    
        
       if event.type == pygame.QUIT:
          run = False
    pygame.display.update()

pygame.quit()

#from game import Game

#g = Game()

#while g.running:
    ## g.curr_menu.display_menu()
    ## g.game_loop()

