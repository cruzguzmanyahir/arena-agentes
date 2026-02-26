import math
import pygame
from agente import Agente


# Inicializar pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agente Móvil con Rotación")
clock = pygame.time.Clock()


# Crear agente
player = Agente(400, 300, 60, angle=30)

MOVE_SPEED = 5
ROTATE_SPEED = 3


running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Convertir ángulo una sola vez
    radians = math.radians(player.angle)
    dir_x = math.cos(radians)
    dir_y = math.sin(radians)

    # Movimiento adelante
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.pos_x += MOVE_SPEED * dir_x
        player.pos_y -= MOVE_SPEED * dir_y

    # Movimiento atrás
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.pos_x -= MOVE_SPEED * dir_x
        player.pos_y += MOVE_SPEED * dir_y

    # Rotación izquierda
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.angle = (player.angle + ROTATE_SPEED) % 360

    # Rotación derecha
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.angle = (player.angle - ROTATE_SPEED) % 360

    # Limitar al borde de la pantalla
    margin = player.size * 1.2
    player.pos_x = max(margin, min(player.pos_x, WIDTH - margin))
    player.pos_y = max(margin, min(player.pos_y, HEIGHT - margin))

    # Dibujar
    ventana.fill((0, 0, 0))
    player.draw(ventana)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()