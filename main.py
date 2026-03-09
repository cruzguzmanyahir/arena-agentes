import pygame
import numpy as np
from agente import NaveTriangular


RESOLUCION = (800, 600)
CUADROS_POR_SEGUNDO = 60

PASO_DESPLAZAMIENTO = 5
PASO_GIRO = 4


class Simulador:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode(RESOLUCION)
        pygame.display.set_caption("Entidad con Transformaciones Matriciales")
        self.reloj = pygame.time.Clock()
        self.activo = True

        w, h = RESOLUCION
        self.objeto = NaveTriangular(w/2, h/2, 60)

    def _entrada_usuario(self):
        teclas = pygame.key.get_pressed()

        direccion = np.array([0.0, 0.0])

        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            direccion += self._vector_frontal()

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            direccion -= self._vector_frontal()

        self.objeto.pos += direccion * PASO_DESPLAZAMIENTO

        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.objeto.rotacion += PASO_GIRO

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.objeto.rotacion -= PASO_GIRO

        self.objeto.rotacion %= 360

    def _vector_frontal(self):
        ang = np.radians(self.objeto.rotacion)
        return np.array([np.cos(ang), -np.sin(ang)])

    def _control_limites(self):
        margen_seguro = self.objeto.escala * 1.1
        ancho, alto = RESOLUCION

        x, y = self.objeto.pos

        if x < margen_seguro:
            x = margen_seguro
            self.objeto.rotacion = 180 - self.objeto.rotacion

        elif x > ancho - margen_seguro:
            x = ancho - margen_seguro
            self.objeto.rotacion = 180 - self.objeto.rotacion

        if y < margen_seguro:
            y = margen_seguro
            self.objeto.rotacion *= -1

        elif y > alto - margen_seguro:
            y = alto - margen_seguro
            self.objeto.rotacion *= -1

        self.objeto.pos = np.array([x, y])
        self.objeto.rotacion %= 360

    def ejecutar(self):
        while self.activo:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.activo = False

            self._entrada_usuario()
            self._control_limites()

            self.ventana.fill((0, 0, 0))
            self.objeto.pintar(self.ventana)

            pygame.display.flip()
            self.reloj.tick(CUADROS_POR_SEGUNDO)

        pygame.quit()


if __name__ == "__main__":
    Simulador().ejecutar()