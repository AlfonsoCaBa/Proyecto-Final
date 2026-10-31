
"""Memory, juego de memoria para encontrar parejas de números."""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')

# Tablero de 4x4 con 8 parejas.
SIZE = 4
TILE_SIZE = 100
TOTAL = SIZE * SIZE
PAIRS = TOTAL // 2

tiles = list(range(PAIRS)) * 2
state = {'mark': None, 'pairs': 0, 'finished': False}
hide = [True] * TOTAL


def square(x, y):
    """Dibuja un cuadrado blanco con borde negro."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(TILE_SIZE)
        left(90)
    end_fill()


def index(x, y):
    """Convierte las coordenadas al índice de una ficha."""
    return int((x + 200) // TILE_SIZE +
               ((y + 200) // TILE_SIZE) * SIZE)


def xy(count):
    """Convierte el índice de una ficha a coordenadas."""
    return (count % SIZE) * TILE_SIZE - 200, \
           (count // SIZE) * TILE_SIZE - 200


def tap(x, y):
    """Actualiza las fichas, cuenta parejas y detecta el fin del juego."""
    if state['finished']:
        return

    # Ignora clics fuera del tablero.
    if not (-200 <= x < 200 and -200 <= y < 200):
        return

    spot = index(x, y)

    # Ignora fichas que ya fueron descubiertas.
    if not hide[spot]:
        return

    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

        # Incrementa el contador al encontrar una pareja.
        state['pairs'] += 1
        print(f"Parejas descubiertas: {state['pairs']}")
        title(f"Memory - Parejas descubiertas: {state['pairs']}/{PAIRS}")

        # Comprueba si todas las fichas están descubiertas.
        if not any(hide):
            state['finished'] = True
            print("¡Felicidades! Descubriste todas las parejas.")
            title("Memory - ¡Juego completado!")


def draw():
    """Dibuja la imagen y las fichas."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(TOTAL):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + TILE_SIZE / 2, y + TILE_SIZE / 4)
        color('black')
        write(tiles[mark], align='center',
              font=('Arial', 40, 'normal'))

    # Muestra un mensaje al completar el juego.
    if state['finished']:
        up()
        goto(0, -15)
        color('green')
        write("¡Ganaste!", align='center',
              font=('Arial', 30, 'bold'))

    update()

    if not state['finished']:
        ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
title(f"Memory - Parejas descubiertas: 0/{PAIRS}")
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
