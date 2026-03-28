import pygame
from agente import NaveTriangular


def iniciar_pygame():
    pygame.init()
    pygame.key.set_repeat(1, 30)


def crear_ventana(resolucion):
    return pygame.display.set_mode(resolucion)


def bucle_principal():
    ANCHO_VENTANA = 800
    ALTO_VENTANA = 600

    pantalla = crear_ventana((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Agente Inteligente - Movimiento y Rotación")

    reloj = pygame.time.Clock()
    jugador = NaveTriangular(ANCHO_VENTANA // 2, ALTO_VENTANA // 2, 60, rotacion_inicial=30)

    activo = True
    while activo:
        tiempo_frame = reloj.tick(60) / 1000.0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                activo = False

        teclado = pygame.key.get_pressed()

        jugador.controlar(tiempo_frame, teclado)
        jugador.limites_pantalla(ANCHO_VENTANA, ALTO_VENTANA)

        pantalla.fill((15, 15, 20))
        jugador.renderizar(pantalla)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    iniciar_pygame()
    bucle_principal()