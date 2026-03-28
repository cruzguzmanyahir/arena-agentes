import math
import pygame
import numpy as np


class NaveTriangular:
    def __init__(self, pos_x, pos_y, escala, rotacion_inicial=0):
        self.centro = np.array([float(pos_x), float(pos_y)], dtype=np.float32)
        self.escala = escala
        self.rotacion = rotacion_inicial % 360

        self.rapidez = 180.0
        self.vector_frontal = np.zeros(2, dtype=np.float32)

    def _recalcular_vector(self):
        ang_rad = math.radians(self.rotacion)
        dir_x = math.cos(ang_rad)
        dir_y = -math.sin(ang_rad)
        self.vector_frontal[:] = (dir_x, dir_y)

    def controlar(self, delta_tiempo, estado_teclas):
        self._recalcular_vector()

        avance = self.vector_frontal * self.rapidez * delta_tiempo

        if estado_teclas[pygame.K_w] or estado_teclas[pygame.K_UP]:
            self.centro += avance

        if estado_teclas[pygame.K_s] or estado_teclas[pygame.K_DOWN]:
            self.centro -= avance

        giro = 120.0 * delta_tiempo

        if estado_teclas[pygame.K_a] or estado_teclas[pygame.K_LEFT]:
            self.rotacion += giro

        if estado_teclas[pygame.K_d] or estado_teclas[pygame.K_RIGHT]:
            self.rotacion -= giro

        self.rotacion %= 360

    def limites_pantalla(self, ancho_ventana, alto_ventana):
        zona_segura = self.escala * 1.2
        colision = False

        x, y = self.centro

        if x <= zona_segura:
            self.centro[0] = zona_segura
            self.rotacion = 180 - self.rotacion
            colision = True

        elif x >= ancho_ventana - zona_segura:
            self.centro[0] = ancho_ventana - zona_segura
            self.rotacion = 180 - self.rotacion
            colision = True

        if y <= zona_segura:
            self.centro[1] = zona_segura
            self.rotacion = -self.rotacion
            colision = True

        elif y >= alto_ventana - zona_segura:
            self.centro[1] = alto_ventana - zona_segura
            self.rotacion = -self.rotacion
            colision = True

        if colision:
            self.rotacion %= 360

    def renderizar(self, superficie, color_figura=(0, 170, 255), color_punta=(255, 80, 80)):
        base = self.escala

        puntos_modelo = [
            (0, -base),
            (-base / 2, base / 2),
            (base / 2, base / 2)
        ]

        rad = math.radians(self.rotacion)
        c = math.cos(rad)
        s = math.sin(rad)

        puntos_finales = []

        for mx, my in puntos_modelo:
            tx = mx * c - my * s
            ty = mx * s + my * c
            puntos_finales.append((
                float(self.centro[0] + tx),
                float(self.centro[1] + ty)
            ))

        pygame.draw.polygon(superficie, color_figura, puntos_finales)
        pygame.draw.polygon(superficie, (255, 255, 255), puntos_finales, 3)

        punta_x, punta_y = puntos_finales[0]
        pygame.draw.circle(superficie, color_punta, (int(punta_x), int(punta_y)), 10)