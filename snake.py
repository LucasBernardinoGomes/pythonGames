import pygame
import random
from pygame.locals import *


def apple_coord_gen():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return x // 10 * 10, y // 10 * 10


def apple_collision(head_position, apple_position):  # Snake X and Y Head coord.
    return head_position == apple_position and head_position == apple_position  # Eating The apple


def collision(head_position, actual_snake):  # Checking for Walls Collision and Body Collision
    if head_position[0] > 600 or head_position[0] < 0 or head_position[1] > 600 or head_position[1] < 0:
        return True
    else:
        for body_position in range(len(actual_snake)-1, 0, -1):
            if head_position == actual_snake[body_position]:
                return True


def movement(actual_snake, snake_direction):
    if snake_direction == UP:
        actual_snake[0] = (snake[0][0], snake[0][1] - 10)
    if snake_direction == DOWN:
        actual_snake[0] = (snake[0][0], snake[0][1] + 10)
    if snake_direction == RIGHT:
        actual_snake[0] = (snake[0][0] + 10, snake[0][1])
    if snake_direction == LEFT:
        actual_snake[0] = (snake[0][0] - 10, snake[0][1])
    return actual_snake


def snake_grow(actual_snake):
    actual_snake.append((-10, -10))
    actual_snake.append((-10, -10))
    return actual_snake


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()  # Initializing PyGame
screen = pygame.display.set_mode((600, 600))  # Screen Size(Height and Weight)
pygame.display.set_caption("Snake")  # Screen Name

apple = pygame.Surface((10, 10))  # Size of the "Object"
apple.fill((255, 0, 0))  # Apple color(RGB)
apple_pos = apple_coord_gen()  # X and Y snake Coordinates

snake = [(200, 200), (210, 200), (220, 200), (230, 200)]  # Snake X and Y coordinates
snake_skin = pygame.Surface((10, 10))  # Size of the "Object"
snake_skin.fill((255, 255, 255))  # Snake color(RGB)

# Initial Directions
my_direction = LEFT
last_direction = RIGHT

clock = pygame.time.Clock()

# -> Loop do Game
while True:
    clock.tick(20)  # -> FPS Number
    for event in pygame.event.get():  # Event Getter
        if event.type == pygame.QUIT:  # When X is Pressed
            pygame.quit()  # Quit Function when Quit pressed

        if event.type == KEYDOWN:
            if event.key == K_UP:
                if last_direction != DOWN:
                    my_direction = UP
            if event.key == K_DOWN:
                if last_direction != UP:
                    my_direction = DOWN
            if event.key == K_LEFT:
                if last_direction != RIGHT:
                    my_direction = LEFT
            if event.key == K_RIGHT:
                if last_direction != LEFT:
                    my_direction = RIGHT

    snake = movement(snake, my_direction)  # Moving the Snake
    last_direction = my_direction

    # Checking for Apple Collision
    if apple_collision(snake[0], apple_pos):
        apple_pos = apple_coord_gen()
        snake = snake_grow(snake)

    # Checking for Wall or Body Collisions
    if collision(snake[0], snake):
        snake = [(200, 200), (210, 200), (220, 200)]
        my_direction = LEFT
        apple_pos = apple_coord_gen()

    # Changing cords. from snake Body(Moving the Snake)
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)  # Plotting the Snake

    pygame.display.update()  # Refreshing the screen
