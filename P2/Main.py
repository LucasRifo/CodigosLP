import pygame
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
"""Colores para utilizar"""
class Fondo(pygame.sprite.Sprite):
    """Clase sprite que va tener todo los metodos y atributos
    del sprite del fondo del juego
    """
    def __init__(self):
        self.imagen = pygame.image.load("suelo.png").convert_alpha()
        self.rect = self.imagen.get_rect()
    def update(self, pantalla, x, y, player):
        #player.Colisiones(self)
        #self.rect.move_ip(-x,-y)
        pantalla.blit(self.imagen,self.rect)

class Objeto(pygame.sprite.Sprite):
    """
    Clase definida para objetos en el entorno, como paredes, obstáculos
    y objetos móviles
    """
    def __init__(self, nombre, pantalla, x0, y0, movible=True):
        self.imagen = pygame.image.load(nombre).convert_alpha()
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = (x0, y0)
        self.movible = movible

    def update(self, pantalla, x, y, fondo, player):
        pantalla.blit(self.imagen,self.rect)
        self.Colision(fondo, player, x, y)

    def Colision(self, fondo, player, x, y):
        if (self.rect.colliderect(player.rect) and
            self.movible == True):
            self.rect.move_ip(x,y)
            """
            Función dedicada a mover objetos móviles al colisionar
            con el personaje
            """

class Player(pygame.sprite.Sprite):
    """
    Clase sprite que va tener todos los metodos y atributos
    del sprite del jugador
    """
    def __init__(self):
        """
        Constructor de la imagen del personaje,
        transformacion de este en un objeto rectangular
        y coordenadas de inicio en la pantalla principal
        """
        self.personaje =  pygame.image.load("personaje.png").convert_alpha()
        self.personaje2 =  pygame.image.load("personaje2.png").convert_alpha()
        self.personaje3 =  pygame.image.load("personaje3.png").convert_alpha()
        self.personaje4 =  pygame.image.load("personaje4.png").convert_alpha()
        self.imagenes = [[self.personaje,self.personaje2,],
                        [self.personaje3,
                        self.personaje4]]
        self.imagen_actual = 0
        self.imagen = self.imagenes[self.imagen_actual][0]
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = (20, 40)
        self.estamoviendo = False
        self.orientacion = 0

    def mover(self,x,y):
        """
        Funcion que realiza el movimiento del sprite
        """
        self.rect.move_ip(x,y)
    def update(self,superficie,x,y,t,fondo, Objetos):
        """Actualiza en la pantalla la imagen que se le entregue"""
        if x == 0 and y == 0: 
            self.estamoviendo = False
        else:
            self.estamoviendo = True

        if x > 0:
            self.orientacion = 0
        elif x < 0:
            self.orientacion = 1

        self.Colisiones(fondo, Objetos)

        if t == 1 and self.estamoviendo:

            self.siguienteimagen()
            
        self.mover(x,y)

        self.imagen = self.imagenes[self.orientacion][self.imagen_actual]

        superficie.blit(self.imagen, self.rect)

    def Colisiones(self,fondo, Objetos):
        for i in range(int(len(Objetos))):
            if (Objetos[i].movible == False and 
                self.rect.colliderect(Objetos[i].rect)):
                if (self.rect.right >= Objetos[i].rect.left and
                    self.rect.left <= Objetos[i].rect.left):
                    self.rect.right = Objetos[i].rect.left
                elif (self.rect.left <= Objetos[i].rect.right and
                    self.rect.right >= Objetos[i].rect.right):
                    self.rect.left = Objetos[i].rect.right
                elif (self.rect.bottom >= Objetos[i].rect.top and
                    self.rect.top <= Objetos[i].rect.top):
                    self.rect.bottom = Objetos[i].rect.top
                elif (self.rect.top <= Objetos[i].rect.bottom and
                    self.rect.bottom >= Objetos[i].rect.bottom):
                    self.rect.top = Objetos[i].rect.bottom
                """
                Compara colisiones con todos los objetos no movibles
                en el mapa
                Tiene problemas al colisionar por arriba o abajo, ya
                que compara primero si colisiona por los lados
                """
        
        if self.rect.right >= fondo.rect.right:
            self.rect.right = fondo.rect.right
        elif self.rect.left <= fondo.rect.left:
            self.rect.left = fondo.rect.left
        if self.rect.bottom >= fondo.rect.bottom:
            self.rect.bottom = fondo.rect.bottom
        elif self.rect.bottom <= fondo.rect.top:
            self.rect.bottom = fondo.rect.top
        """
        Tomando en cuenta las medidas de la imagen de fondo,
        evita que el personaje salga del mapa
        """

    def siguienteimagen(self):

        """Realiza el cambio de imagen para la animacion del personaje
        """
        self.imagen_actual += 1
        if self.imagen_actual > (len(self.imagenes) - 1):
            self.imagen_actual = 0

def main():
    """
    Funcion que conlleva todo el manejo del programa,
    con el uso de lo que se vera o no en la pantalla, y los tipos
    de eventos
    """

    pygame.init()
    pantalla = pygame.display.set_mode((600,500))
    salir = False
    reloj = pygame.time.Clock()
    """Variables de entorno del juego"""

    player = Player()
    fondo = Fondo()
    Objetos = []
    objeto = Objeto("Cuadrado.png",pantalla, 170, 110)
    Objetos.append(objeto)
    objeto = Objeto("CuadradoRojo.png",pantalla, 110, 150, False)
    Objetos.append(objeto)
    """
    Objetos declarados en el juego, podría llamarse a niveles
    prehechos para ahorrar código en el Main
    """

    x, y = 0, 0
    velocidad = 3
    leftsigueapretada = False
    rightsigueapretada = False
    upsigueapretada = False
    downsigueapretada = False
    t = 0
    """Variables de uso del juego"""

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada = True
                    x = -velocidad
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada = True
                    x = velocidad
                if event.key == pygame.K_UP:
                    upsigueapretada = True
                    y = -velocidad
                if event.key == pygame.K_DOWN:
                    downsigueapretada = True
                    y = velocidad

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada = False
                    if rightsigueapretada:
                        x = velocidad
                    else:
                        x = 0
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada = False
                    if leftsigueapretada:
                        x = -velocidad
                    else:
                        x = 0
                if event.key == pygame.K_UP:
                    upsigueapretada = False
                    if downsigueapretada:
                        y = velocidad
                    else:
                        y = 0
                if event.key == pygame.K_DOWN:
                    downsigueapretada = False
                    if upsigueapretada:
                        y = -velocidad
                    else:
                        y = 0
            """Posibles inputs dentro del juego"""


        reloj.tick(30)
        t += 1
        if t >2:  # que imagen se va a colocar
            t = 0

        pantalla.fill((BLACK))
        fondo.update(pantalla, x, y, player)
        player.update(pantalla, x, y, t, fondo, Objetos)
        for i in range(int(len(Objetos))):
            Objetos[i].update(pantalla, x, y, fondo, player)
        pygame.display.update()


    pygame.quit()
main()