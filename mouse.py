class Pointer(object):

	def __init__(self,x,y):
		self.x=x
		self.y=y

	def moveUp(self):
		self.y += 1	

	def moveDown(self):
		self.y -= 1

	def moveLeft(self):
		self.x -= 1

	def moveRight(self):
		self.x += 1	

	def check(self):
		x=self.x
		y=self.y
		print(x,y)	


#adding the comment to see the git changes stuffs		