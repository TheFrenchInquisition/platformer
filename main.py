import pygame, sys

class physobj(object):
	def __init__(self,screen,pos=None,gravity=True):
		self.screen = screen
		self.pos = pos

	def move(self,newvel=None):
		x = self.pos[0]
		y = self.pos[1]

		if newvel == None:
			vel = self.vel
		else:
			vel = newvel

		dir = vel[1]

		while dir > 4:
			dir -= 4

		if dir <= 1:
			xweight = dir
			yweight = -(1 - dir)
		elif dir <= 2:
			xweight = 2 - dir
			yweight = dir - 1
		elif dir <= 3:
			xweight = -(dir - 2)
			yweight = 3 - dir
		else:
			xweight = -(4 - dir)
			yweight = -(dir - 3)
		
		x += vel[0] * xweight
		y += vel[0] * yweight
		self.pos = (x, y)

	def destroy(self):
		self.destroy()

	def drawobj(self):
		pygame.draw.rect(self.screen, (255, 0, 0), (self.pos[0], self.pos[1], 20, 20))

class player(physobj):
	def __init__(self,screen,pos,gravity=True):
		physobj.__init__(self,screen,pos)

class main:
	def __init__(self,width=400,height=400):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()

		pygame.display.set_caption("platformer")

		self.objlist = []

		player0 = player(self.screen, (190, 190))

		self.objlist.append(player0)

	def loop(self):
		while True:
			self.clock.tick(120)

			self.screen.fill((0, 0, 0))

			keys = pygame.key.get_pressed()
			if keys[pygame.K_d]:
				self.objlist[0].move((1, 1))
			if keys[pygame.K_a]:
				self.objlist[0].move((1, 3))

			#Draw Objects

			for i in range(len(self.objlist)):
				self.objlist[i].drawobj()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			pygame.display.update()

if __name__ == "__main__":
	MainWindow = main()
	MainWindow.loop()