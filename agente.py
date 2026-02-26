import math
import pygame


class Agente:
    def __init__(self, pos_x, pos_y, size, angle=30):
        """
        Crea un agente con:
        - pos_x, pos_y : posición en pantalla
        - size         : tamaño del triángulo
        - angle        : ángulo en grados
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size
        self.angle = angle

    def draw(self, ventana, body_color=(0, 180, 0), front_color=(255, 50, 50)):
        """
        Dibuja el agente como un triángulo rotado.
        """

        # Triángulo base (apuntando hacia arriba)
        local_points = [
            (0, -self.size),                  # punta frontal
            (-self.size / 2, self.size / 2),  # esquina izquierda
            (self.size / 2, self.size / 2)    # esquina derecha
        ]

        # Convertir ángulo a radianes
        radians = math.radians(self.angle)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)

        # Aplicar rotación
        rotated_points = []
        for x, y in local_points:
            new_x = x * cos_angle - y * sin_angle
            new_y = x * sin_angle + y * cos_angle
            rotated_points.append((self.pos_x + new_x, self.pos_y + new_y))

        # Dibujar triángulo
        pygame.draw.polygon(ventana, body_color, rotated_points)
        pygame.draw.polygon(ventana, (255, 255, 255), rotated_points, 3)

        # Dibujar círculo frontal
        front_x, front_y = rotated_points[0]
        pygame.draw.circle(ventana, front_color, (int(front_x), int(front_y)), 10)