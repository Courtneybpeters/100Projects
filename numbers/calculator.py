import math
import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((300, 450))
pygame.display.set_caption("Calculator")


#Colors:
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)


while True:
	screen.fill(black)

	screen_rect = pygame.draw.rect()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()



