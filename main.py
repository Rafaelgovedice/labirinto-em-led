from microbit import *

# Coordenadas iniciais da bolinha
x = 0
y = 0

# Desenha o labirinto (1s são paredes, 0s são caminhos)
labirinto = [
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0]
]

def desenhar_labirinto():
    for i in range(5):
        for j in range(5):
            if labirinto[j][i] == 1:
                display.set_pixel(i, j, 2)  # Paredes com brilho médio

def atualizar_bolinha():
    display.set_pixel(x, y, 9)  # Bolinha com brilho máximo

while True:
    desenhar_labirinto()
    atualizar_bolinha()
    
    sleep(200)
    display.clear()
    
    desenhar_labirinto()  # Desenhar novamente o labirinto após limpar a tela

    # Lê a inclinação do acelerômetro
    if accelerometer.get_x() > 200 and x < 4 and labirinto[y][x + 1] == 0:
        x += 1
    elif accelerometer.get_x() < -200 and x > 0 and labirinto[y][x - 1] == 0:
        x -= 1
    elif accelerometer.get_y() > 200 and y < 4 and labirinto[y + 1][x] == 0:
        y += 1
    elif accelerometer.get_y() < -200 and y > 0 and labirinto[y - 1][x] == 0:
        y -= 1

    # Verifica se chegou ao ponto final
    if x == 4 and y == 4:
        display.scroll("Venceu!")
        break

