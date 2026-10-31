
"""Juego de gato (Tic Tac Toe)."""

from turtle import *
from freegames import line


def grid():
    """Dibuja la cuadrícula del juego."""
    color('black')
    width(1)
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


state = {'player': 0, 'finished': False}
players = [drawx, drawo]
occupied = set()
board = {}  # Guarda qué jugador ocupa cada casilla.


def check_winner():
    """Comprueba si existen tres símbolos iguales en línea."""
    # Posibles combinaciones ganadoras: filas, columnas y diagonales.
    combinations = [
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]

    for combination in combinations:
        a, b, c = combination

        if a in board and b in board and c in board:
            if board[a] == board[b] == board[c]:
                return board[a]

    return None


def show_result(message):
    """Muestra el resultado del juego en la ventana."""
    state['finished'] = True
    color('black')
    up()
    goto(0, -195)
    write(message, align='center', font=('Arial', 14, 'bold'))
    update()


def tap(x, y):
    """Realiza una jugada si la casilla está libre y el juego continúa."""
    if state['finished']:
        return

    x = floor(x)
    y = floor(y)

    # Evita seleccionar posiciones fuera del tablero.
    if x not in (-200, -67, 66) or y not in (-200, -67, 66):
        return

    # Evita dibujar sobre una casilla ocupada.
    if (x, y) in occupied:
        return

    player = state['player']
    draw = players[player]
    draw(x, y)

    occupied.add((x, y))

    # Convierte las coordenadas en índices de 0 a 2.
    col = (x + 200) // 133
    row = (y + 200) // 133
    board[(col, row)] = player

    update()

    # Comprueba si el jugador actual ganó.
    winner = check_winner()

    if winner is not None:
        symbol = 'X' if winner == 0 else 'O'
        show_result(f'¡Ganó el jugador {symbol}!')
        return

    # Si las nueve casillas están ocupadas y nadie ganó, hay empate.
    if len(occupied) == 9:
        show_result('¡Empate!')
        return

    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
