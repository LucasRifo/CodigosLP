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
"""
Titulo="Título"
Ancho = 640
Alto = 480
Para imprimir el título?"""

Tamaño_Jugador = 40
Color1 = BLUE
Color2 = RED
x1=200
y1=300
x2=700
y2=300
"""Condiciones de Spawn iniciales"""

"""
BULLETWIDTH = 5
BULLETHEIGHT = 5
BULLETOFFSET = 700
Propiedades de los Disparos?"""

Direcciones = {pygame.K_LEFT  : (-1),
               pygame.K_RIGHT : (1),
               pygame.K_UP : (-1),
               pygame.K_DOWN: (1)}
"""Para que los inputs no se interlapsen"""

class Player1(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.width = Tamaño_Jugador
		self.image = pygame.Surface((self.width, self.width))
		self.color = Color1
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.name = PLAYER1
		self.speed = 3
		self.vectorx = 0
		self.vectory = 0

	def update(self, keys, *args):
        for key in Direcciones:
            if keys[key]:
                self.rect.x += Direcciones[key] * self.speed
                
        self.Check_Colisiones()
        self.image.fill(self.color)

    def Check_Colisiones(self):
        if self.rect.right > Ancho:
            self.rect.right = Ancho
            self.vectorx = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.vectorx = 0

class Player2(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.width = Tamaño_Jugador
		self.image = pygame.Surface((self.width, self.width))
		self.color = Color2
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.name = PLAYER2
		self.speed = 3
		self.vectorx = 0
		self.vectory = 0

	def update(self, keys, *args):
        for key in Direcciones:
            if keys[key]:
                self.rect.x += Direcciones[key] * self.speed
                
        self.Check_Colisiones()
        self.image.fill(self.color)

    def Check_Colisiones(self):
        if self.rect.right > Ancho:
            self.rect.right = Ancho
            self.vectorx = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.vectorx = 0