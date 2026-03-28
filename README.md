# Proyecto de Graficación — Agente Triangular en Movimiento

## 📌 Descripción General

Este proyecto implementa una figura triangular que actúa como un agente móvil dentro de un entorno gráfico.

El sistema permite simular movimiento vectorial en tiempo real utilizando rotación y desplazamiento relativo a la orientación actual del objeto.

---

## 🎯 Funcionalidades

El agente triangular puede:

- Rotar sobre su propio eje
- Avanzar en la dirección hacia donde apunta
- Retroceder en sentido contrario
- Rebotar automáticamente al colisionar con los bordes de la ventana
- Mantener movimiento suave mediante control por delta de tiempo

---

## 📂 Estructura del Proyecto

### 🔹 agente.py
Define la clase principal del objeto móvil.

Responsabilidades:

- Gestionar posición y orientación
- Calcular dirección de movimiento con trigonometría
- Aplicar desplazamiento vectorial
- Detectar colisiones con límites de pantalla
- Renderizar el triángulo con rotación dinámica

---

### 🔹 main.py
Archivo principal del programa.

Se encarga de:

- Inicializar Pygame
- Crear la ventana gráfica
- Capturar eventos del teclado
- Ejecutar el bucle principal del juego
- Actualizar estado del agente
- Dibujar en pantalla cada fotograma

---

## 🎮 Controles de Movimiento

| Tecla | Acción |
|------|--------|
| W / ↑ | Avanzar |
| S / ↓ | Retroceder |
| A / ← | Rotar a la izquierda |
| D / → | Rotar a la derecha |

---

## 🧰 Librerías Utilizadas

- **pygame** → Renderizado y control de eventos
- **math** → Cálculos trigonométricos
- **numpy** → Manejo eficiente de vectores

---

## ⚙️ Requisitos

Instalar dependencias:

```bash
pip install pygame numpy