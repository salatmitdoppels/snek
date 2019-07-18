# import pygame
import random
import os
import msvcrt
import time
import pickle

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

screenWidth = 800
screenHeith = 600
rows = 25
columns = 40
grid = [['  ' for x in range(columns)] for y in range(rows)]
apple = []
snek = [[]]
snek_direction = [0, 0]
key = "x"
alive = True
if os.path.isfile('conf.dat'):
    with open('conf.dat', 'r+b') as f:
        highscore = pickle.load(f)
else:
    with open('conf.dat', 'x+b') as f:
        highscore = []
        pickle.dump(highscore, f)


def main():
    global snek, apple, snek_direction, key, alive, highscore
    reset()
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getwch()
            if key == 'à':
                key = msvcrt.getwch()
        if key == "\x1b":  # ESC
            break
        if key == "\r":
            reset()
        if alive:
            alive = move(key)
        else:
            score = [input("name? ").ljust(25)[:25], len(snek)]
            for i in range(len(highscore)):
                if score[1] > highscore[i][1]:
                    highscore.insert(i, score)
                    break
            else:
                highscore.append(score)
            with open('conf.dat', 'w+b') as f:
                pickle.dump(highscore, f)
            reset()
        draw()
        time.sleep(0.05)


def reset():
    global snek, grid, apple, snek_direction, key, alive
    snek = [new_apple()]
    apple = new_apple()
    snek_direction = [0, 0]
    alive = True
    key = 'x'


def move(key):
    global snek, apple, snek_direction
    if (key == 'a' or key == 'K') and snek_direction[0] == 0:
        snek_direction = [-1, 0]
    if (key == 'd' or key == 'M') and snek_direction[0] == 0:
        snek_direction = [1, 0]
    if (key == 'w' or key == 'H') and snek_direction[1] == 0:
        snek_direction = [0, -1]
    if (key == 's' or key == 'P') and snek_direction[1] == 0:
        snek_direction = [0, 1]
    newhead = [
        snek[0][0] + snek_direction[0],
        snek[0][1] + snek_direction[1]
    ]
    for i in range(1, len(snek)):
        if newhead == snek[i]:
            return False
    if (
            newhead[0] >= columns or
            newhead[0] < 0 or
            newhead[1] >= rows or
            newhead[1] < 0
    ):
        return False
    else:
        snek = [newhead] + snek
        if(newhead == apple):
            apple = new_apple()
        else:
            del snek[-1]
        return True


def new_apple():
    leer = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '  ':
                leer.append([x, y])
    return random.choice(leer)


def draw():
    global grid, screen, snek, highscore
    grid = [['  ' for y in range(columns)] for x in range(rows)]
    for i in range(len(snek)):
        x = snek[i][0]
        y = snek[i][1]
        if (i == 0):
            grid[y][x] = '██'
        else:
            grid[y][x] = '██'
    grid[apple[1]][apple[0]] = 'CD'
    clear()
    print('╔', end='')
    for _ in range(columns):
        print('══', end='')
    print('╗' + ' Highscore!')
    for i in range(len(grid)):
        print('║', end='')
        print(*grid[i], sep='', end='')
        print('║', end='')
        if len(highscore) > i:
            print(' ' + (str(i+1) + '. ').ljust(5)[:5], end='')
            print(*highscore[i])
        else:
            print()
    print('╚', end='')
    for _ in range(columns):
        print('══', end='')
    print('╝')
    print(len(snek))
    '''
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                color = BLACK
            elif grid[x][y] == 1:
                color = YELLOW
            elif grid[x][y] == 2:
                color = WHITE
            elif grid[x][y] == 3:
                color = RED
    '''


def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


main()
