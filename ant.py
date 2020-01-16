import pygame

pygame.init()
height = 800
width = 600
grid = []
newgrid = []
row = []

gameloop = True
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
antx = 5
anty = 6
clock = pygame.time.Clock()
direction = 3
window = pygame.display.set_mode((height, width))
pygame.display.set_caption("Langton's Ant")
newgrid = grid

for i in range(11):
    row = []
    for j in range(15):
        row.append(0)
    grid.append(row)


def crawl(antx, anty, direction):

    if grid[antx % 11][anty % 15] == 0:
        newgrid[antx % 11][anty % 15] = 1
        if direction == 0:
            antx = (antx+1) % 15
            direction = (direction+1) % 4
        elif direction == 1:
            anty = (anty+1) % 15
            direction = (direction+1) % 4
        elif direction == 2:
            antx = (antx-1) % 15
            direction = (direction+1) % 4
        elif direction == 3:
            anty = (anty-1) % 15
            direction = (direction+1) % 4
    else:
        newgrid[antx % 11][anty % 15] = 0

        if direction == 0:
            antx = (antx-1) % 15
            direction = (direction-1+4) % 4
        elif direction == 1:
            anty = (anty-1) % 15
            direction = (direction-1+4) % 4
        elif direction == 2:
            antx = (antx+1) % 15
            direction = (direction-1+4) % 4
        elif direction == 3:
            anty = (anty+1) % 15
            direction = (direction-1+4) % 4
    return antx, anty, direction


# print(grid)
while gameloop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            gameloop = False

    window.fill(white)

    for i in range(11):
        for j in range(15):
            if grid[i][j] == 0:
                pygame.draw.rect(window, (0, 0, 0), [
                    20+(j*50), 20+(i*50), 50, 50], 1)
            else:
                pygame.draw.rect(window, (0, 0, 0), [
                    20+(j*50), 20+(i*50), 50, 50])
           # pygame.draw.rect(window, red, (antx, anty, 20, 20))
    clock.tick(30)
    # pygame.draw.rect(window,black,())
    antx, anty, direction = crawl(antx, anty, direction)
    grid = newgrid
    pygame.display.update()
