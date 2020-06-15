import sys
import pygame
import random
import time
from pygame.sprite import Group
from snake import Snake_pcs
from snake_settings import Settings
import snake_game_functions as gf

def draw_grid():
	global screen
	rows=20
	x=30
	y=30
	for row in range(rows+1):
		pygame.draw.line(screen,(255,255,255),(x*row,0),(x*row,600))
		pygame.draw.line(screen,(255,255,255),(0,y*row),(600,y*row))

def run_snake_game():
	global screen
	pygame.init()
	screen=pygame.display.set_mode((600,600))
	pygame.display.set_caption("snake game")
	clock=pygame.time.Clock()
	snakes=Group()
	settings=Settings()
	snake_body=[]
	snake1=Snake_pcs(settings,screen)
	snake_body.append(snake1)
	snakes.add(snake1)
	food = Snake_pcs(settings,screen)
	
	while True:
		gf.check_events(snakes,settings)
		gf.snake_col_self(snake_body,snakes,settings)
		if settings.run_game:
			gf.create_food(settings,food,snakes)
			new_snake=Snake_pcs(settings,screen)
			gf.snake_food_collide(new_snake,settings,snake_body,snakes,food)
			if not settings.food_vis:
				gf.move_snake(snake_body,snakes,settings,new_snake)
			gf.wall_collide(snake_body,settings)	
			
		
		screen.fill((169,169,169))
		draw_grid()
		food.draw_food()
		for snake in snakes.sprites():
			snake.draw_snake()
		pygame.display.flip()
		pygame.time.delay(100)
		clock.tick(50)
		
		
run_snake_game()	
