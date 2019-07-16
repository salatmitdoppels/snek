import pygame
import random
# import os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

screenWidth = 800
screenHeith = 600
rows = 30
columns = 40
grid = [[0 for x in range(rows)] for y in range(columns)]
# print(grid)
apple = []
snek = [[]]
# print(snek)
snek_direction = [0, 0]
new_snek_direction = [0, 0]


def main():
    global snek, apple, screen, snek_direction, new_snek_direction, font
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeith))
    pygame.display.set_caption('Snek')
    font = pygame.font.SysFont('Sans', 50)
    clock = pygame.time.Clock()
    crashed = False
    snek = [new_apple()]
    apple = new_apple()
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                new_snek_direction = [0, 0]
                snek = [new_apple()]
                apple = new_apple()
        while move() and not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if snek_direction[1] == 0:
                            new_snek_direction = [0, -1]
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if snek_direction[1] == 0:
                            new_snek_direction = [0, 1]
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if snek_direction[0] == 0:
                            new_snek_direction = [-1, 0]
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if snek_direction[0] == 0:
                            new_snek_direction = [1, 0]
                # print(event)
            draw()
            pygame.display.flip()
            clock.tick(20)


def move():
    global snek, apple, snek_direction, new_snek_direction
    # print(snek)
    # print(new_snek_direction)
    # print(snek_direction)
    snek_direction = new_snek_direction
    newhead = [
        snek[0][0] + snek_direction[0],
        snek[0][1] + snek_direction[1]
    ]
    for i in range(1, len(snek)):
        if newhead == snek[i]:
            return False
    if (
            newhead[1] >= rows or
            newhead[1] < 0 or
            newhead[0] >= columns or
            newhead[0] < 0
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
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                leer.append([x, y])
    apple = random.choice(leer)
    return apple


def draw():
    global grid, screen, snek
    grid = [[0 for x in range(rows)] for x in range(columns)]
    for i in range(len(snek)):
        x = snek[i][0]
        y = snek[i][1]
        if (i == 0):
            grid[x][y] = 1
        else:
            grid[x][y] = 2
    grid[apple[0]][apple[1]] = 3
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
            pygame.draw.rect(screen, color, [
                x * screenWidth / columns,
                y * screenHeith / rows,
                screenWidth / columns,
                screenHeith / rows
            ])
    text = font.render(str(len(snek)), True, WHITE)
    screen.blit(
        text, (
            screenWidth - 50,
            screenHeith - 50
        )
    )


def highscore():
    pass


main()
