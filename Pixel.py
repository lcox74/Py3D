import pygame

class Pixel:
	def __init__ (self, x, y, col):
		self.x = x
		self.y = y
		self.col = col

	def draw (self, surface, res):
		pygame.draw.rect(surface, self.col, (self.x * res, self.y * res, res, res))