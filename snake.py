import pygame
from pygame.sprite import Sprite

class Snake_pcs(Sprite):
	
	def __init__(self,settings,screen):
		super().__init__()
		self.settings=settings
		self.screen=screen
		
		self.rect=pygame.Rect(self.settings.pos[0]+1,self.settings.pos[1]+1,self.settings.s_width-1,self.settings.s_height-1)
		
	def draw_food(self):
		pygame.draw.rect(self.screen,(150,100,50),self.rect)	
		
	def draw_snake(self):
		pygame.draw.rect(self.screen,(0,255,0),self.rect)	
		
		
	
