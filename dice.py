import pygame
import probas

pygame.init()

WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('CaviarDreams.ttf', 18)

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
        if self.selected:
            pygame.draw.rect(screen, (143, 201, 163), [
                             self.x_pos, self.y_pos, 100, 100], 4, 5)
            
    def check_click(self, coordinates):
        if self.die.collidepoint(coordinates):
            if dice_selected[self.key]:
                dice_selected[self.key] = False
            elif not dice_selected[self.key]:
                dice_selected[self.key] = True


def draw_dice(dices_array):
    for die in range(len(dices_array)):
        dices_array[die].draw()
    

def main_draw():
    timer = pygame.time.Clock()
    fps = 60
    dice_values = [0, 0, 0, 0, 0]
    global dice_selected
    dice_selected = [False, False, False, False, False]
    roll = False
    rolls_left = 3
    running = True
    while running:
        timer.tick(fps)
        screen.fill((100, 20, 55))
        #BUTTON ROL
        button_roll = pygame.draw.rect(screen, (255, 245, 238), [250, 185, 100, 50])
        roll_text = font.render('ROLL', True, (60, 25, 29))
        screen.blit(roll_text, (280, 200))
        #ROLLS LEFT TEXT 
        turns_text = font.render('Rolls Left This Turn: ' + str(rolls_left), True, (255, 245, 238))
        screen.blit(turns_text, (15, 15))
        #DICE
        dice1 = Dice(10, 50, dice_values[0], 0)
        dice2 = Dice(130, 50, dice_values[1], 1)
        dice3 = Dice(250, 50, dice_values[2], 2)
        dice4 = Dice(370, 50, dice_values[3], 3)
        dice5 = Dice(490, 50, dice_values[4], 4)
        dices_array = [dice1, dice2, dice3, dice4, dice5]
        draw_dice(dices_array)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for value in range(len(dices_array)):
                    dices_array[value].check_click(event.pos)
                if button_roll.collidepoint(event.pos)and rolls_left > 0:
                    roll = True  
                    rolls_left -= 1
        if roll:
            for value in range(len(dice_values)):
                if not dice_selected[value]:
                    dice_values[value] = probas.uniformdisc(1, 6)
            roll = False

        pygame.display.flip()

#Uncomment for testing the file
#main_draw()