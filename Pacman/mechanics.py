import pygame

def CheckDirection(event, x_change, y_change) -> list[int]:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change, y_change = [-3, 0]
        if event.key == pygame.K_RIGHT:
            x_change, y_change = [3, 0]
        if event.key == pygame.K_UP:
            x_change, y_change = [0, -3]
        if event.key == pygame.K_DOWN:
            x_change, y_change = [0, 3]

    return [x_change, y_change]

