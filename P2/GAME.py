import pygame
import sys
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((900,500))

GRAY      = (100, 100, 100)
NAVYBLUE  = ( 60,  60, 100)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
YELLOW    = (255, 255,   0)
ORANGE    = (255, 128,   0)
PURPLE    = (255,   0, 255)
CYAN      = (  0, 255, 255)
BLACK     = (  0,   0,   0)
NEARBLACK = ( 19,  15,  48)
COMBLUE   = (233, 232, 255)
"""Lista de colores que puedo utilizar"""

Tamaño_Jugador = 40
Color1 = BLUE
Color2 = RED
x1=200
y1=300
x2=700
y2=300
"""Condiciones de Spawn iniciales"""

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.QUIT()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			Color2 = not Color2
		if event.type == pygame.KEYDOWN and event.key == 47:
			Color1 = not Color1

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		y1 += -3
	if pressed[pygame.K_DOWN]:
		y1 += 3
	if pressed[pygame.K_LEFT]:
		x1 += -3
	if pressed[pygame.K_RIGHT]:
		x1 += 3
	if pressed[119]:
		y2 += -3
	if pressed[115]:
		y2 += 3
	if pressed[97]:
		x2 += -3
	if pressed[100]:
		x2 += 3

	if Color1:
		color_rect1 = BLUE
	else:
		color_rect1 = WHITE
	if Color2:
		color_rect2 = RED
	else:
		color_rect2 = ORANGE

	screen.fill(BLACK)
	pygame.draw.rect(screen,color_rect1,pygame.Rect(x1,y1,Tamaño_Jugador,Tamaño_Jugador))
	pygame.draw.rect(screen,color_rect2,pygame.Rect(x2,y2,Tamaño_Jugador,Tamaño_Jugador))

	pygame.display.flip()
	clock.tick(60)
pygame.quit()