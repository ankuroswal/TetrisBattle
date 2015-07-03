import pygame
import random
import time

#necessary pygame initializing
pygame.init()

#define screen size
SCREEN_SIZE_x = 600
SCREEN_SIZE_y = 600

#gridsize
GRID_SIZE = 15

#create a surface that will be seen by the user
screen =  pygame.display.set_mode((SCREEN_SIZE_x, SCREEN_SIZE_y))

#init clock
clock = pygame.time.Clock()

#random seed
random.seed()

#colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
PURP = (135, 0, 255)

#music
#pygame.mixer.music.load('bb-game.mid')
#pygame.mixer.music.play(-1, 0)


#init pieces
straight = [[0, 0, 0, 0], [1, 1, 1, 1]]
Lr = [[0, 0, 1, 0], [1, 1, 1, 0]]
Ll = [[1, 1, 1, 0], [0, 0, 1, 0]]
Zr = [[0, 1, 1, 0], [1, 1, 0, 0]]
Zl = [[1, 1, 0, 0], [0, 1, 1, 0]]
box = [[1, 1, 0, 0], [1, 1, 0, 0]]

currentOrientation = 0


done = False

def draw_piece(x, y, o, p, color):
	curcursor_x = x
	curcursor_y = y

	#draw game piece

	if o == 0:
		for z in range(0, 4):
			if p[0][z] == 1:
				pygame.draw.rect(screen, color, (curcursor_x, curcursor_y, 15, 15))

			if p[1][z] == 1:
				pygame.draw.rect(screen, color, (curcursor_x, curcursor_y + GRID_SIZE, 15, 15))

			curcursor_x += 15
	elif o == 1:
		for z in range(0, 4):
			if p[0][z] == 1:
				pygame.draw.rect(screen, color, (curcursor_x + GRID_SIZE, curcursor_y, 15, 15))

			if p[1][z] == 1:
				pygame.draw.rect(screen, color, (curcursor_x, curcursor_y, 15, 15))

			curcursor_y += 15
	elif o == 2:
		for z in range(0, 4):
			if p[0][z] == 1:
				pygame.draw.rect(screen, color, (curcursor_x, curcursor_y + GRID_SIZE, 15, 15))

			if p[1][z] == 1:
				pygame.draw.rect(screen, color, (curcursor_x, curcursor_y, 15, 15))

			curcursor_x -= 15

	elif o == 3:
		for z in range(0, 4):
			if p[0][z] == 1:
				pygame.draw.rect(screen, color, (curcursor_x, curcursor_y, 15, 15))

			if p[1][z] == 1:
				pygame.draw.rect(screen, color, (curcursor_x + GRID_SIZE, curcursor_y, 15, 15))

			curcursor_y -= 15






while not done:
	#white background
	screen.fill(WHITE)

	draw_piece(150, 150, 0, Lr, PURP)
	
	draw_piece(325, 325, 1, Zr, BLACK)

	draw_piece(200, 400, 2, Lr, PURP)

	draw_piece(400, 100, 3, Lr, BLACK)


	#score text
	#font = pygame.font.Font(None, 36)
	#score_txt = font.render("Score: " + str(score), 1, (10, 10, 10))
	#screen.blit(score_txt, (260, 36))


	#for event in pygame.event.get():  # User did something
	#	if event.type == pygame.QUIT:  # If user clicked close
	#		done = True  # Flag that we are done so we exit this loop	
	#	if event.type == pygame.KEYDOWN:
	#		if (event.key == pygame.K_UP and not head_direction == 0):
	#			head_direction = 2
	#			#head[0] = int((head[0] / SNAKE_SIZE)) * SNAKE_SIZE
	#		elif (event.key == pygame.K_RIGHT and not head_direction == 3):
	#			head_direction = 1
	#			#head[1] = int((head[1] / SNAKE_SIZE)) * SNAKE_SIZE
	#		elif (event.key == pygame.K_DOWN and not head_direction == 2):
	#			head_direction = 0
	#			#head[0] = int((head[0] / SNAKE_SIZE)) * SNAKE_SIZE
	#		elif (event.key == pygame.K_LEFT and not head_direction == 1):
	#			head_direction = 3
	#			#head[1] = int((head[1] / SNAKE_SIZE)) * SNAKE_SIZE

	pygame.display.flip()

	clock.tick(15)


pygame.quit()




