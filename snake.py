import pygame
import random
from pygame.locals import *


def apple_coord_gen():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return x // 10 * 10, y // 10 * 10


def apple_collision(snakeHead, apple):  # Snake X and Y Head coord.
    return snakeHead == apple and snakeHead == apple  # Eating The apple


def wall_collision(snakeHead):  # Checking for Walls Colision
    if (snakeHead[0] > 600 or snakeHead[0] < 0) or (snakeHead[1] > 600 or snakeHead[1] < 0):
        return True


def movement(snake, my_direction):
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    return snake


def snake_grow(snake):
    snake.append((-10, -10))
    snake.append((-10, -10))
    snake.append((-10, -10))
    return snake


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()  # Initializing PyGame
screen = pygame.display.set_mode((600, 600))  # Screen Size(Height and Weight)
pygame.display.set_caption("Snake Window")  # Screen Name

apple = pygame.Surface((10, 10))  # Size of the "Object"
apple.fill((255, 0, 0))  # Apple color(RGB)
apple_pos = apple_coord_gen()  # Snake X and Y coordinates

snake = [(200, 200), (210, 200), (220, 200), (230, 200)]  # X and Y snake Coordinates
snake_skin = pygame.Surface((10, 10))  # Size of the "Object"
snake_skin.fill((255, 255, 255))  # Snake color(RGB)
my_direction = LEFT  # Initial Direction

# Fps control
clock = pygame.time.Clock()

# -> Loop do Game
while True:
    clock.tick(20)  # -> FPS Number

    for event in pygame.event.get():  # Event Getter
        if event.type == pygame.QUIT:  # When X is Pressed
            pygame.quit()  # Quit Function when Quit pressed

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    snake = movement(snake, my_direction)  # Moving the Snake

    # Checking or Apple
    if apple_collision(snake[0], apple_pos):
        apple_pos = apple_coord_gen()
        snake = snake_grow(snake)

    # Checking for Wall Collisions
    elif wall_collision(snake[0]):
        snake = [(200, 200), (210, 200), (220, 200)]
        apple_pos = apple_coord_gen()

    # Changing cords. from snake Body(Moving the Snake)
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)  # Plotting the Snake

    pygame.display.update()  # Refreshing the screen
