import pygame
import abc
import random

# Define la interfaz Dibujable
class Dibujable(abc.ABC):
    @abc.abstractmethod
    def dibujar(self, pantalla):
        pass

# Clase base de las Figuras
class Figura(Dibujable):
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Se da un color aleatorio a cada figura

# Clase Círculo
class Circulo(Figura):
    def dibujar(self, pantalla):
        radio = ((self.punto2[0] - self.punto1[0])**2 + (self.punto2[1] - self.punto1[1])**2) ** 0.5
        pygame.draw.circle(pantalla, self.color, self.punto1, int(radio))

# Clase Triángulo
class Triangulo(Figura):
    def dibujar(self, pantalla):
        pygame.draw.polygon(pantalla, self.color, [self.punto1, (self.punto1[0], self.punto2[1]), self.punto2])

# Clase Rectángulo
class Rectangulo(Figura):
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.punto1[0], self.punto1[1], 
                                                self.punto2[0] - self.punto1[0],
                                                self.punto2[1] - self.punto1[1]))

# Inicio Pygame
pygame.init()

# Tamaño de la interfaz 
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Dibujando Figuras")

# Bucle principal
running = True
figuras = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            punto1 = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            punto2 = pygame.mouse.get_pos()
            figura = random.choice([Circulo(punto1, punto2), Triangulo(punto1, punto2), Rectangulo(punto1, punto2)])
            figuras.append(figura)

    pantalla.fill((0, 0, 0))  # Le coloco fondo negro para que se vean mejor las figuras

    for figura in figuras:
        figura.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()
