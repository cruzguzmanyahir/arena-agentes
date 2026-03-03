# Proyecto – Simulación de Entidad Rotatoria

## Descripción General

Este proyecto implementa una entidad gráfica con forma triangular que puede:

- Rotar sobre su propio eje
- Avanzar y retroceder según su orientación
- Rebotar automáticamente al colisionar con los bordes de la ventana

El desarrollo fue realizado utilizando la librería `pygame`.

---

## Estructura del Proyecto

### 1. agente.py

Contiene la clase `EntidadMovil`, encargada de:

- Administrar posición mediante `pygame.Vector2`
- Manejar la orientación en grados
- Calcular la rotación del triángulo usando funciones trigonométricas
- Dibujar el polígono rotado en pantalla

Se utiliza una transformación manual basada en seno y coseno para aplicar rotación sobre los vértices definidos localmente.

---

### 2. main.py

Gestiona:

- Inicialización del entorno gráfico
- Control del teclado
- Movimiento y rotación
- Detección de colisiones con bordes
- Refresco de pantalla

La lógica fue modularizada en funciones independientes:

- `procesar_movimiento()`
- `procesar_rotacion()`
- `verificar_limites()`

Esto mejora la legibilidad y organización del código.

---

## Controles

| Tecla | Acción |
|-------|--------|
| W / ↑ | Avanzar |
| S / ↓ | Retroceder |
| A / ← | Rotar izquierda |
| D / → | Rotar derecha |

---

## Comportamiento del Rebote

Cuando la entidad toca un borde:

- Se corrige su posición
- Se ajusta su ángulo de dirección
- Se normaliza el ángulo en un rango de 0° a 360°

Esto permite simular un rebote dinámico realista.

---

## Posibles Mejoras Futuras

- Implementar aceleración e inercia
- Agregar múltiples entidades
- Añadir detección de colisiones entre objetos
- Incorporar disparos o interacción adicional
