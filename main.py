import random
from sys import exit

import pygame

TILE_SIZE = 25
ROWS = 25
COLUMNS = ROWS
GAME_WIDTH = TILE_SIZE * COLUMNS
GAME_HEIGHT = TILE_SIZE * ROWS

pygame.init()

window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


def _get_random(limit):
    return random.randint(0, limit - 1) * TILE_SIZE


food = pygame.Rect(_get_random(COLUMNS), _get_random(ROWS), TILE_SIZE, TILE_SIZE)
snake = []
snake.append(pygame.Rect(_get_random(COLUMNS), _get_random(ROWS), TILE_SIZE, TILE_SIZE))

snake_velocity = (0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                snake_velocity = (0, -TILE_SIZE)
            if event.key in (pygame.K_DOWN, pygame.K_s):
                snake_velocity = (0, TILE_SIZE)
            if event.key in (pygame.K_LEFT, pygame.K_a):
                snake_velocity = (-TILE_SIZE, 0)
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                snake_velocity = (TILE_SIZE, 0)

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1].copy()

    snake[0].move_ip(snake_velocity)

    if snake[0].center == food.center:
        snake.append(food)
        food = pygame.Rect(
            _get_random(COLUMNS), _get_random(ROWS), TILE_SIZE, TILE_SIZE
        )

    if not window.get_rect().contains(snake[0]):
        food = pygame.Rect(
            _get_random(COLUMNS), _get_random(ROWS), TILE_SIZE, TILE_SIZE
        )
        snake.clear()
        snake.append(
            pygame.Rect(_get_random(COLUMNS), _get_random(ROWS), TILE_SIZE, TILE_SIZE)
        )

    window.fill("black")

    pygame.draw.rect(window, "yellow", food)

    for snake_part in snake:
        pygame.draw.rect(window, "cyan", snake_part)

    pygame.display.update()
    clock.tick(10)
