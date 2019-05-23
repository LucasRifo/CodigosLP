import pygame
pygame.init()
screen = pygame.display.set_mode((900,500))

is_blue = False
color_rect = (0,128,255)
x=500
y=80

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.QUIT()
		if event.type == pygame.KEYDOWN:
			is_blue = not is_blue
			print(event.key)
	
	if is_blue:
		color_rect = (0,128,255)
	else:
		color_rect = (255,128,0)

	pygame.draw.rect(screen,color_rect,pygame.Rect(x,y,60,60))

	pygame.display.flip()
pygame.quit()