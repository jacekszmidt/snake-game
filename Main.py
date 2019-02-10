from enum import Enum

import pygame
from pygame.math import Vector2

import random


class SnakeMove(Enum):
    UP = Vector2(0, -10)
    DOWN = Vector2(0, 10)
    LEFT = Vector2(-10, 0)
    RIGHT = Vector2(10, 0)


class Snake:
    def __init__(self):
        self.position = Vector2(200, 200)
        self.snake_size = 10
        self.next_move = SnakeMove.UP
        self.snake_color = (0, 0, 0)

    def move(self, game_display):
        self.set_next_pos()
        print(f'current pos {self.position.x}:{self.position.y}')
        pygame.draw.rect(game_display, self.snake_color,
                         (self.position.x, self.position.y,
                          self.snake_size, self.snake_size))

    def set_next_pos(self):
        if self.next_move == SnakeMove.UP:
            self.position += SnakeMove.UP.value
        if self.next_move == SnakeMove.DOWN:
            self.position += SnakeMove.DOWN.value
        if self.next_move == SnakeMove.LEFT:
            self.position += SnakeMove.LEFT.value
        if self.next_move == SnakeMove.RIGHT:
            self.position += SnakeMove.RIGHT.value

    def go_up(self):
        self.next_move = SnakeMove.UP

    def go_down(self):
        self.next_move = SnakeMove.DOWN

    def go_left(self):
        self.next_move = SnakeMove.LEFT

    def go_right(self):
        self.next_move = SnakeMove.RIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.stop_game = False
        self.bg_color = [255, 255, 255]
        self.fps_number = 4
        self.display_width = 600
        self.display_height = 480
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Snake_Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()

    def handle_keyboard_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    self.stop_game = True
                if event.key == pygame.K_LEFT:
                    self.snake.go_left()
                if event.key == pygame.K_RIGHT:
                    self.snake.go_right()
                if event.key == pygame.K_UP:
                    self.snake.go_up()
                if event.key == pygame.K_DOWN:
                    self.snake.go_down()
                if event.key == pygame.K_ESCAPE:
                    self.stop_game = True

    def play(self):
        while not self.stop_game:
            self.game_display.fill(self.bg_color)
            self.handle_keyboard_input()
            self.snake.move(self.game_display)
            self.clock.tick(self.fps_number)
            self.food.eating_food()
            self.food.printing_food(self.game_display)
            pygame.display.update()
            self.game_over()

    def game_over(self):
        if self.snake.position.x >= self.display_width\
                or self.snake.position.y >= self.display_height\
                or self.snake.position.x >= self.snake.position.x*3.2\
                or self.snake.position.y >= self.snake.position.y*2.4:
            self.stop_game = True
            print("Game Over!")
        else:
            pass


class Food:
    def __init__(self):
        self.x_food = 10 * (random.randint(0, 600 / 10) - 1)
        self.y_food = 10 * (random.randint(0, 480 / 10) - 1)
        self.snake = Snake()
        self.eaten_food = False

    def printing_food(self, display):
        pygame.draw.rect(display, (0, 0, 255), (self.x_food, self.y_food, 10, 10), 0)

    def eating_food(self):
        if self.x_food == self.snake.position.x and self.y_food == self.snake.position.y:
                self.eaten_food = True
                self.x_food = 10 * (random.randint(0, 600 / 10) - 1)
                self.y_food = 10 * (random.randint(0, 480 / 10) - 1)


Game().play()
