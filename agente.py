import pygame
import numpy as np
from math import radians, sin, cos


class NaveTriangular:
    def __init__(self, px, py, escala_figura, orientacion=30):
        self.pos = np.array([px, py], dtype=float)
        self.escala = escala_figura
        self.rotacion = orientacion

    def _modelo_local(self):
        return np.array([
            [0, -self.escala],
            [-self.escala * 0.5, self.escala * 0.5],
            [self.escala * 0.5, self.escala * 0.5]
        ])

    def _matriz_rotacion(self):
        ang = radians(self.rotacion)
        return np.array([
            [cos(ang), -sin(ang)],
            [sin(ang),  cos(ang)]
        ])

    def obtener_vertices(self):
        figura = self._modelo_local()
        giro = self._matriz_rotacion()
        rotados = figura @ giro
        trasladados = rotados + self.pos
        return trasladados

    def pintar(self, lienzo, color_fig=(0,160,0), color_dir=(255,60,60)):
        puntos = self.obtener_vertices()

        pygame.draw.polygon(lienzo, color_fig, puntos)
        pygame.draw.polygon(lienzo, (255,255,255), puntos, 2)

        punta = puntos[0]
        pygame.draw.circle(lienzo, color_dir, (int(punta[0]), int(punta[1])), 9)