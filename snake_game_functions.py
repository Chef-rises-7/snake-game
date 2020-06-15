import sys
import random
import pygame
# i have 20 rows and columns.
def check_events(snakes,settings):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				settings.dirx=0
				settings.diry=-1
			elif event.key == pygame.K_DOWN:
				settings.dirx=0
				settings.diry=1
			elif event.key == pygame.K_LEFT:
				settings.dirx=-1
				settings.diry=0
			elif event.key == pygame.K_RIGHT:
				settings.dirx=1
				settings.diry=0
			elif event.key == pygame.K_q:
				sys.exit()	
				
def move_snake(snake_body,snakes,settings,new_snake):
	rem_snake=snake_body.pop(-1)
	snakes.remove(rem_snake)
	new_snake.rect.x=settings.pos[0]+30*settings.dirx+1
	new_snake.rect.y=settings.pos[1]+30*settings.diry+1
	settings.pos[0]=settings.pos[0]+30*settings.dirx
	settings.pos[1]=settings.pos[1]+30*settings.diry
	snake_body.insert(0,new_snake)
	snakes.add(new_snake)				
					
def create_food(settings,food,snakes):
	if settings.food_vis:
		rand_food(food,snakes)
		while pygame.sprite.spritecollideany(food,snakes):
			rand_food(food,snakes)
		settings.food_vis=False					

def snake_food_collide(new_snake,settings,snake_body,snakes,food):
	if snake_body[0].rect == food.rect:
		settings.food_vis=True
		new_snake.rect.x=settings.pos[0]+30*settings.dirx+1
		new_snake.rect.y=settings.pos[1]+30*settings.diry+1				
		settings.pos[0]=settings.pos[0]+30*settings.dirx
		settings.pos[1]=settings.pos[1]+30*settings.diry
		snake_body.insert(0,new_snake)
		snakes.add(new_snake)
						
def rand_food(food,snakes):
	x=random.randrange(0,19)*30
	y=random.randrange(0,19)*30
	food.rect.x=x+1
	food.rect.y=y+1
	
	
def wall_collide(snake_body,settings):
	if(snake_body[0].rect.x<0):
		snake_body[0].rect.x=571
		settings.pos[0]=570
	elif(snake_body[0].rect.x>600):
		snake_body[0].rect.x=1
		settings.pos[0]=0
	elif(snake_body[0].rect.y<0):
		snake_body[0].rect.y=571
		settings.pos[1]=570
	elif(snake_body[0].rect.y>600):
		snake_body[0].rect.y=1
		settings.pos[1]=0
	
	
def snake_col_self(snake_body,snakes,settings):
	for i in range(1,len(snake_body)):
		if snake_body[0].rect == snake_body[i].rect:
			settings.run_game=False
			
		
		
	
	
	
	
	
	
	
		
		
		
		
		
						
