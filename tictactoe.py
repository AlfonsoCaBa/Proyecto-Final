
"""Juego de gato (Tic Tac Toe)."""

from turtle import *
from freegames import line


def grid():
    """Dibuja la cuadrícula del juego."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja una X azul, centrada y con tamaño reducido."""
    color('blue')
    width(5)
    # Margen de 20 píxeles para centrar la X en la casilla.
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)


def drawo(x, y):
    """Dibuja una O roja, centrada y con tamaño reducido."""
    color('red')
    width(5)
    up()
    # Radio de 46 píxeles para centrar la O en la casilla.
    goto(x + 66.5, y + 20.5)
    down()
    circle(46)


def floor(value):
    """Redondea la coordenada hacia abajo a una casilla de tamaño 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
occupied = set()  # Guarda las coordenadas de las casillas ocupadas.


def tap(x, y):
    """Dibuja una X o una O únicamente si la casilla está libre."""
    x = floor(x)
    y = floor(y)

    # Evita dibujar sobre una casilla que ya fue seleccionada.
    if (x, y) in occupied:
        return

    player = state['player']
    draw = players[player]
    draw(x, y)

    # Registra la casilla como ocupada.
    occupied.add((x, y))

    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
