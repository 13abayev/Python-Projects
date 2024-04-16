import pygame
pygame.init()
from math import pi
from maze import my_maze
from Entities import Player, Enemy

from mechanics import CheckDirection

blue = (70,52,236)
yellow = (255,255,147)
black = (5,5,5)
pink = (251, 156, 250)


screen_size = (960,650)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("./Images/PacMan")
game_icon = pygame.image.load("./Images/game.png")
pygame.display.set_icon(game_icon)



def DrawMaze():
    cell_size = 40
    posY = 0
    for line in my_maze:
        posX = 0
        for block in line:
            if block == 1 :
                pygame.draw.circle(screen, yellow, (posX + cell_size/2, posY + cell_size/2), 4)
            elif block == 2 :
                pygame.draw.circle(screen, yellow, (posX + cell_size/2, posY + cell_size/2), 8)
            elif block == 3 :
                pygame.draw.line(screen, blue, (posX, posY + cell_size/2),(posX + cell_size, posY + cell_size/2),3)
            elif block == 4:
                pygame.draw.line(screen, blue, (posX + cell_size/2, posY), (posX + cell_size/2, posY + cell_size),3)
            elif block == 5:
                pygame.draw.arc(screen, blue, [(posX - cell_size*0.45), (posY - cell_size*0.45), cell_size, cell_size], 3*pi/2, 2*pi, 3)
            elif block == 6:
                pygame.draw.arc(screen, blue, [(posX + cell_size/2), (posY - cell_size * 0.44), cell_size, cell_size], pi, 3*pi/2, 3)
            elif block == 7:
                pygame.draw.arc(screen, blue, [(posX - cell_size/2), (posY + cell_size/2), cell_size, cell_size], 0, pi/2, 3)
            elif block == 8:
                pygame.draw.arc(screen, blue, [(posX + cell_size/2), (posY + cell_size/2), cell_size, cell_size], pi/2, pi ,3)
            elif block == 9 :
                pygame.draw.line(screen, pink, (posX, posY + cell_size/2),(posX + cell_size, posY + cell_size/2),4)
            posX += cell_size
        posY += cell_size
            

def LocatePlayer(x, y, icon):
    screen.blit(icon, (x, y))

running = True
clock = pygame.time.Clock()
fps = 60

x_change = 0
y_change = 0


player = Player(11* 40 - 30, 11 * 40 - 10, pygame.image.load("./Images/pacman.png"))


while running:
    clock.tick(fps)
    screen.fill(black)
    DrawMaze()
    LocatePlayer(player.x, player.y, player.icon)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        x_change, y_change = CheckDirection(event, x_change, y_change)

    y = (player.y + y_change + 10)//40
    x = (player.x + x_change + 30)//40
    if my_maze[y][x] in [0, 1, 2]:
        player.x += x_change
        player.y += y_change
        if my_maze[y][x] == 1:
            my_maze[y][x] = 0
            player.score += 10
        
        
        
    pygame.display.flip()