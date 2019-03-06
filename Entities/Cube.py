import pygame
from Entity import Entity, Mesh, Triangle

class Cube(Entity):
	def __init__ (self, x = 0, y = 0, z = 0):
		Entity.__init__(self, 'Cube', x, y, z)

		self.mesh.LoadObj("Model\\mountains.obj")

		# self.mesh.tris = [
		# 	#South
		# 	Triangle((0, 0, 0), (0, 1, 0), (1, 1, 0)),
		# 	Triangle((0, 0, 0), (1, 1, 0), (1, 0, 0)),

		# 	#East
		# 	Triangle((1, 0, 0), (1, 1, 0), (1, 1, 1)),
		# 	Triangle((1, 0, 0), (1, 1, 1), (1, 0, 1)),

		# 	#North
		# 	Triangle((1, 0, 1), (1, 1, 1), (0, 1, 1)),
		# 	Triangle((1, 0, 1), (0, 1, 1), (0, 0, 1)),

		# 	#West
		# 	Triangle((0, 0, 1), (0, 1, 1), (0, 1, 0)),
		# 	Triangle((0, 0, 1), (0, 1, 0), (0, 0, 0)),

		# 	#Top
		# 	Triangle((0, 1, 0), (0, 1, 1), (1, 1, 1)),
		# 	Triangle((0, 1, 0), (1, 1, 1), (1, 1, 0)),

		# 	#Bottom
		# 	Triangle((1, 0, 1), (0, 0, 1), (0, 0, 0)),
		# 	Triangle((1, 0, 1), (0, 0, 0), (1, 0, 0))
		# ]
	