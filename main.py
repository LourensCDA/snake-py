import random
from sys import exit

import pygame

# --- Grid configuration -------------------------------------------------------
# The board is a square grid of ROWS x COLUMNS tiles; everything moves in
# whole-tile steps so the snake and food always stay aligned to the grid.
TILE_SIZE = 25
ROWS = 25
COLUMNS = ROWS
GAME_WIDTH = TILE_SIZE * COLUMNS
GAME_HEIGHT = TILE_SIZE * ROWS

# --- Pygame setup -------------------------------------------------------------
# Create the window sized to the grid and a clock to cap the frame rate.
pygame.init()

window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


# --- Helpers ------------------------------------------------------------------
def _get_random(limit):
    """Return a random pixel coordinate snapped to a tile boundary within limit tiles."""
    return random.randint(0, limit - 1) * TILE_SIZE


# --- Initial game state -------------------------------------------------------
# One food tile and a single-segment snake, both placed at random grid positions.
# The snake starts stationary until the player presses a direction key.
food = pygame.Rect(_get_random(COLUMNS), _get_random(ROWS), TILE_SIZE, TILE_SIZE)
snake = []
snake.append(pygame.Rect(_get_random(COLUMNS), _get_random(ROWS), TILE_SIZE, TILE_SIZE))

snake_velocity = (0, 0)

# --- Main game loop -----------------------------------------------------------
while True:
    # Input: close the window on QUIT, or change direction on arrow / WASD keys.
    # Velocity is one tile per frame along a single axis.
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

    # Movement: shift each body segment into the position of the one ahead of it
    # (working from tail to head), then move the head by the current velocity.
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1].copy()

    snake[0].move_ip(snake_velocity)

    # Eating: when the head lands on the food, the food rect becomes a new tail
    # segment and a fresh food tile is spawned elsewhere.
    if snake[0].center == food.center:
        snake.append(food)
        food = pygame.Rect(
            _get_random(COLUMNS), _get_random(ROWS), TILE_SIZE, TILE_SIZE
        )

    # Wall collision: leaving the window resets the game to a new random
    # single-segment snake and new food.
    if not window.get_rect().contains(snake[0]):
        food = pygame.Rect(
            _get_random(COLUMNS), _get_random(ROWS), TILE_SIZE, TILE_SIZE
        )
        snake.clear()
        snake.append(
            pygame.Rect(_get_random(COLUMNS), _get_random(ROWS), TILE_SIZE, TILE_SIZE)
        )

    # Rendering: clear the screen, draw the food and every snake segment, then
    # present the frame and hold the loop to 10 frames per second.
    window.fill("black")

    pygame.draw.rect(window, "yellow", food)

    for snake_part in snake:
        pygame.draw.rect(window, "cyan", snake_part)

    pygame.display.update()
    clock.tick(10)
