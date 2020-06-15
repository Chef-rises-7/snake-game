class Settings():
	def __init__(self):
		self.snake_color=(0,255,0)
		self.s_width=30
		self.s_height=30
		self.reset_stats()
		
		
		
	def reset_stats(self):	
		self.dirx=1
		self.diry=0
		self.pos=[240,240]
		self.food_vis=True
		self.run_game=True
