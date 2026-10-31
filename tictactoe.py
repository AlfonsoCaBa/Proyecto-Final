
"""Juego de gato (Tic Tac Toe).

Ejercicios originales:

1. Dar a las X y O diferentes colores y grosores.
2. ¿Qué sucede cuando alguien selecciona una casilla ocupada?
3. ¿Cómo detectar cuando alguien ha ganado?
4. ¿Cómo crear un jugador controlado por la computadora?
"""

from turtle import *
from freegames import line


def grid():
    """Dibuja la cuadrícula del juego."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja la X del jugador."""
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Dibuja la O del jugador."""
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Redondea la coordenada hacia abajo a una casilla de tamaño 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Dibuja una X o una O en la casilla seleccionada."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
