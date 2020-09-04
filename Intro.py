# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 22:06:54 2020

@author: SHUBH ASHISH
"""

import pygame
import time
import random

pygame.init()

color = (255, 255, 255)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

icon = pygame.image.load('samosa.png')
pygame.display.set_icon(icon)

img = pygame.image.load('head.png')
samosa = pygame.image.load('samosa.png')
clock = pygame.time.Clock()
block_size = 30
FPS = 20
font = pygame.font.SysFont(None, 35)
direction = 'right'
smallfont = pygame.font.SysFont('helvetica', 25)
medfont = pygame.font.SysFont('helvetica', 50)
largefont = pygame.font.SysFont('helvetica', 80)

def message_to_screen(msg, color, y_displace = 0, size = 'small'):
	textSurf, textRect = text_objects(msg, color, size)
	textRect.center = (display_width/2), (display_height/2)+y_displace
	gameDisplay.blit(textSurf, textRect)

def pause():
	paused = True
	gameDisplay.fill((255, 255, 255))
	message_to_screen('Paused',
						(0, 0, 0),
						-100,
						size = 'large')
	message_to_screen('Press C to continue or Q to quit',
						(0, 0, 0),
						25)
	pygame.display.update()
	clock.tick(10)

	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
	

def score(score):
	text = smallfont.render("Score: "+str(score), True, (0, 0, 0))
	gameDisplay.blit(text, [0,0])

def game_intro():
	intro = True
	while intro:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_c:
					intro = False

		gameDisplay.fill(color)
		message_to_screen('Welcome to snake',
							(130, 180, 90),
							-100,
							size = 'large')
		message_to_screen('Eat the red apples.',
							(0, 0, 0),
							-30)
		message_to_screen('The more apples you eat, the longer you get.',
							(0, 0, 0),
							10)
		message_to_screen('Don\'t run into yourself or the border.',
							(0, 0, 0),
							40)
		message_to_screen('Press C to play or Q to quit.',
							(240, 20, 0),
							90,
							size = 'medium')
		pygame.display.update()
		clock.tick(30)

def snake(block_size, snake_list):
	if direction == 'right':
		head = pygame.transform.rotate(img, 270)
	elif direction == 'left':
		head = pygame.transform.rotate(img, 90)
	elif direction == 'up':
		head = img
	else:
		head = pygame.transform.rotate(img, 180)

	gameDisplay.blit(head, (snake_list[-1][0], snake_list[-1][1]))

	for XnY in snake_list[:-3]:
		pygame.draw.rect(gameDisplay, (114, 194, 33), [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):
	if size == 'small':
		textSurf = smallfont.render(text, True, color)
	elif size == 'medium':
		textSurf = medfont.render(text, True, color)
	elif size == 'large':
		textSurf = largefont.render(text, True, color)
	
	return textSurf, textSurf.get_rect()


	

	# screen_text = font.render(msg, True, color)
	# gameDisplay.blit(screen_text, [int(display_width/2), int(display_height/2)])

def apple_generator():
	position_apple_X = round(random.randrange(0, display_width - block_size)/10.0)*10.0
	position_apple_Y = round(random.randrange(0, display_height - block_size)/10.0)*10.0

	return position_apple_X, position_apple_Y

def gameloop():
	global direction
	snake_list = []
	snake_length = 1
	gameExit = False
	gameOver = False
	lead_x_change = 0
	lead_x = int(display_width/2)
	lead_y = int(display_height/2)
	lead_y_change = 0
	
	position_apple_X, position_apple_Y = apple_generator()

	while not gameExit:
		while gameOver == True:
			gameDisplay.fill(color)
			message_to_screen("Game Over!", (255, 210, 70), -50, size = 'large')
			message_to_screen("Press C to play again or Q to quit", (0, 255, 0), 50, size = 'medium')
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameloop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -10
					lead_y_change = 0
					direction = 'left'
				if event.key == pygame.K_RIGHT:
					lead_x_change = 10
					lead_y_change = 0
					direction = 'right'
				if event.key == pygame.K_UP:
					lead_y_change = -10
					lead_x_change = 0
					direction = 'up'
				if event.key == pygame.K_DOWN:
					lead_y_change = 10
					lead_x_change = 0
					direction = 'down'	
				if event.key == pygame.K_p:
					pause()
		if lead_x < 0 or lead_x >= display_width or lead_y < 0 or lead_y >= display_height:
			gameOver = True
		lead_x += lead_x_change
		lead_y += lead_y_change
		gameDisplay.fill(color)
		#pygame.draw.rect(gameDisplay, (0, 255, 0), [position_apple_X, position_apple_Y, block_size, block_size])

		gameDisplay.blit(samosa, (position_apple_X, position_apple_Y))
		snake_head = []
		snake_head.append(lead_x)
		snake_head.append(lead_y)
		snake_list.append(snake_head)

		if len(snake_list) > snake_length:
			del snake_list[0]
		snake(block_size, snake_list)

		for each_segment in snake_list[:-1]:
			if each_segment == snake_head:
				gameOver = True
		
		score(snake_length - 1)
		pygame.display.update()

		# if (lead_x >= position_apple_X and lead_x <= position_apple_X + block_size):
		# 	if (lead_y >= position_apple_Y and lead_y <= position_apple_Y + block_size): 			#This is just to see if the snake is in the range of apple's height and width so that it does not only eat it when the initial pos match
		# 		snake_length += 3
		# 		position_apple_X = round(random.randrange(0, display_width - block_size)/10.0)*10.0
		# 		position_apple_Y = round(random.randrange(0, display_height - block_size)/10.0)*10.0

		if lead_x >= position_apple_X and lead_x <= position_apple_X + block_size or lead_x + block_size >= position_apple_X and lead_x + block_size <= position_apple_X + block_size:
			if lead_y >= position_apple_Y and lead_y <= position_apple_Y + block_size or lead_y + block_size >= position_apple_Y and lead_y + block_size <= position_apple_Y + block_size:
				snake_length += 3
				position_apple_X, position_apple_Y = apple_generator()
		clock.tick(FPS)
	pygame.quit()
	quit()

game_intro()
gameloop()
	