"""
Importing important libraries
"""
import pygame
import probas
import dice
import functions
import opponent
import os


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
				dice.Dice.pick = probas.uniformdisc
				dice.Dice.pick_params = [1, 6]
				dice.main_draw()
				oppo = opponent.Opponent(level-1)
				oppo.calculate_score()
				# Affichage des scores

		if button_lvl2.collidepoint((mx, my)):
			if click:
				click = False
				level = 2
				level_proba = run_lvl2(click)
				dice.Dice.pick = probas.binomdice
				dice.Dice.pick_params = [level_proba]
				dice.main_draw()
				oppo = opponent.Opponent(level-1)
				oppo.calculate_score()
				# Affichage des scores

		if button_lvl3.collidepoint((mx, my)):
			if click:
				click = False
				level = 3
				level_proba = run_lvl(
					"Choose a number between 1 and 6", click)
				dice.Dice.pick = probas.poissondice
				dice.Dice.pick_params = [level_proba]
				dice.main_draw()
				oppo = opponent.Opponent(level-1)
				oppo.calculate_score()
				# Affichage des scores

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


"""
LEVEL 2 - BINOMIALE
"""


def run_lvl2(click):
	proba = choose_proba("Choose a probability between 0 and 1")
	print(proba)
	running = True
	while running:
		screen.fill((114, 47, 55))
		functions.draw_text('proba : ' + str(proba), font,
							(255, 245, 238), screen, 140, 32)

		# Two variables to keep the position of the mouse
		mx, my = pygame.mouse.get_pos()
		# starting button // little fonction later ?
		button_start = pygame.Rect(200, 100, 200, 50)
		pygame.draw.rect(screen, (255, 245, 238), button_start)
		functions.draw_text('START GAME', font, (60, 25, 29), screen, 250, 115)

		if button_start.collidepoint((mx, my)):
			if click:
				running = False

		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

	return proba


"""
LEVEL 1 UNIFORME - 3 POISSON
"""


def run_lvl(instruction, click):
	proba = choose_proba(instruction)
	print(proba)
	running = True
	while running:
		screen.fill((114, 47, 55))
		functions.draw_text('proba : ' + str(proba), font,
							(255, 245, 238), screen, 140, 32)

		# Two variables to keep the position of the mouse
		mx, my = pygame.mouse.get_pos()
		# starting button // little fonction later ?
		button_start = pygame.Rect(200, 100, 200, 50)
		pygame.draw.rect(screen, (255, 245, 238), button_start)
		functions.draw_text('START GAME', font, (60, 25, 29), screen, 250, 115)

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
Function for the user to choose the probability wanted
"""


def choose_proba(instruction):
	input_proba = pygame.Rect(250, 250, 140, 32)
	proba_chosen = ''
	color_active = pygame.Color((60, 25, 29))
	color_passive = pygame.Color('white')
	color = color_passive
	active = False
	global level
	print(level)

	running = True

	while running:
		screen.fill((114, 47, 55))
		functions.draw_text(instruction, font,
							(255, 245, 238), screen, 150, 200)
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
				elif event.key != pygame.K_KP_ENTER or event.key != pygame.K_RETURN:
					proba_chosen += event.unicode
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					if level == 2:
						try:
							proba = float(proba_chosen)
							if 0 <= proba <= 1:
								return proba
							else:
								msg = "The probability must be bewteen 0 and 1"
								print(msg)
								functions.draw_text(msg, font, (255, 245, 238),
													screen, 150, 200)
								proba_chosen = ''
						except ValueError:
							errorMsg = "Error : The probability must be bewteen 0 and 1"
							print(errorMsg)
							functions.draw_text(errorMsg, font, (255, 245, 238),
												screen, 150, 200)
							proba_chosen = ''
					elif level == 3:
						try:
							proba = float(proba_chosen)
							if 0 <= proba <= 6:
								return proba
							else:
								msg = "The number must be between 1 and 6"
								print(msg)
								functions.draw_text(msg, font, (255, 245, 238),
													screen, 150, 200)
								proba_chosen = ''
						except ValueError:
							errorMsg = "Error : The number must be between 1 and 6"
							print(errorMsg)
							functions.draw_text(errorMsg, font, (255, 245, 238),
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


"""
END FUNCTIONS
"""

main_menu()

pygame.quit()
