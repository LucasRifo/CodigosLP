import pygame
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((900,500))
is_blue = False
color_rect = (0,128,255)
x=500
y=80

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.QUIT()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			is_blue = not is_blue

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		y += -3
	if pressed[pygame.K_DOWN]:
		y += 3
	if pressed[pygame.K_LEFT]:
		x += -3
	if pressed[pygame.K_RIGHT]:
		x += 3

	if is_blue:
		color_rect = (0,128,255)
	else:
		color_rect = (255,128,0)

	screen.fill((0,0,0))
	pygame.draw.rect(screen,color_rect,pygame.Rect(x,y,60,60))

	pygame.display.flip()
	clock.tick(60)
pygame.quit()