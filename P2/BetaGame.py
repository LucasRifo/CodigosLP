import pygame
import sys

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
x1 = 200
y1 = 300
x2 = 700
y2 = 300
"""Condiciones de Spawn iniciales"""

Direcciones={pygame.K_UP:-1,pygame.K_DOWN:1,pygame.K_LEFT:-1,pygame.K_RIGHT:1}

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        self.dimensión = Tamaño_Jugador
        self.imagen = pygame.Surface(self.dimensión,self.dimensión)
        self.color = Color1
        self.imagen.fill(color)
        self.rect = self.image.get_rect()
        self.nombre = "Player1"
        self.velocidad = 3
        self.vectorX = 0
    def Actualizar(self,keys,*args):
        for key in Direcciones:
            if keys[key]:
                self.rectx  += DIRECT_DICT[key] * self.speed
        self.Colisiones()
        self.imagen.fill(self.color)
    def Colisiones(self):
        if self.rect.right > 500:
            self.rect.right = 500
            self.vectorX = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.vectorX = 0
class App(Elemento):
    def __init__(self):
        pygame.init()
        #clock = pygame.time.Clock()
        self.displaySurf, self.displayRect = self.makeScreen()
        self.GameStart = True
        self.GameOver = False
        self.BeginGame = False

    def ResetGame(self):
        self.GameStart = True
        self.MensajeIntro1 = Text('orena.tff',25,'Bienvenido',GREEN,self.displayRect,self.displaySurf)
        self.MensajeIntro2 = Text('orena.tff',20,'Bienvenido',GREEN,self.displayRect,self.displaySurf)
        self.MensajeIntro2.rect.top = self.MensajeIntro1.rect.bottom + 5
        self.MensajeGameOver = Text('orena.tff',25,'Game Over',GREEN,self.displayRect,self.displaySurf)
        self.player1 = self.CrearPlayer()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
pygame.quit()