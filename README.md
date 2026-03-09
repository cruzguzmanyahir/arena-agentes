# Simulación de Movimiento con Transformaciones 2D

## Resumen

Este proyecto desarrolla una figura triangular interactiva que puede desplazarse y rotar dentro de una ventana gráfica.  
El sistema incluye detección de colisiones contra los bordes y respuesta automática tipo rebote.

La implementación utiliza Python junto con la librería Pygame y operaciones matriciales con NumPy.

---

## Organización del Código

### agente.py

Define la clase `NaveTriangular`, responsable de:

- Gestionar posición y orientación
- Construir la geometría local del triángulo
- Aplicar rotación mediante matrices 2x2
- Realizar traslación a coordenadas globales
- Dibujar la figura y su indicador de dirección

Se emplea multiplicación matricial para transformar los vértices.

---

### main.py

Contiene la clase `Simulador`, que administra:

- Ventana y ciclo principal
- Lectura de teclado
- Movimiento relativo a la orientación
- Rotación angular
- Validación de límites de pantalla
- Actualización de renderizado

El diseño es orientado a objetos para separar responsabilidades.

---

## Controles de Usuario

| Tecla | Función |
|------|---------|
| W / ↑ | Avanzar |
| S / ↓ | Retroceder |
| A / ← | Giro antihorario |
| D / → | Giro horario |

---

## Sistema de Colisiones

Al detectar contacto con los bordes:

- Se reajusta la posición al límite permitido
- Se modifica el ángulo de movimiento
- Se normaliza el valor angular

Esto produce un efecto de rebote consistente.

---

## Tecnologías Utilizadas

- Python
- Pygame
- NumPy

---

## Posibles Extensiones

- Física con aceleración
- Multiples entidades simultáneas
- Colisiones entre objetos
- Sistema de proyectiles
- Escenarios dinámicos