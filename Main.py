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
        self.position_list = list()
        self.position_list.append(Vector2(200, 200))
        self.snake_size = 10
        self.next_move = SnakeMove.UP
        self.snake_color = (0, 0, 0)

    def move(self, game_display):
        self.set_next_pos()
        print(f'current pos {self.position_list[0].x}:{self.position_list[0].y}')
        pygame.draw.rect(game_display, self.snake_color,
                         (self.position_list[0].x, self.position_list[0].y,
                          self.snake_size, self.snake_size,))

    def set_next_pos(self):
        if self.next_move == SnakeMove.UP:
            self.position_list[0] += SnakeMove.UP.value
        if self.next_move == SnakeMove.DOWN:
            self.position_list[0] += SnakeMove.DOWN.value
        if self.next_move == SnakeMove.LEFT:
            self.position_list[0] += SnakeMove.LEFT.value
        if self.next_move == SnakeMove.RIGHT:
            self.position_list[0] += SnakeMove.RIGHT.value

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
        self.score = 0
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Snake_Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food(self.snake)

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
            self.display_score(self.game_display)
            pygame.display.update()
            self.game_over()

    def game_over(self):
        if self.snake.position_list[0].x >= self.display_width\
                or self.snake.position_list[0].y >= self.display_height\
                or self.snake.position_list[0].x >= self.snake.position_list[0].x*3.2\
                or self.snake.position_list[0].y >= self.snake.position_list[0].y*2.4:
            self.stop_game = True
            print("Game Over!")
        else:
            pass

    def display_score(self, game_display):
        font = pygame.font.SysFont("arial", 15)
        text = font.render(f"Score: {self.food.score}", True, (135, 135, 205))
        self.game_display.blit(text, (10, 10))


class Food:
    def __init__(self, snake):
        self.x_food = 10 * (random.randint(0, 600 / 10) - 1)  # food every 10px: 110x120, 130x150
        self.y_food = 10 * (random.randint(0, 480 / 10) - 1)
        self.eaten_food = False
        self.snake = snake
        self.score = 0
        self.snake.add_snake = False

    def printing_food(self, display):
        pygame.draw.rect(display, (0, 0, 255), (self.x_food, self.y_food, 10, 10), 0)

    def eating_food(self):
        if self.x_food == self.snake.position_list[0].x and self.y_food == self.snake.position_list[0].y:  # checking position
                self.eaten_food = True
                self.score += 1  # counting points
                print(self.score)
                self.x_food = 10 * (random.randint(0, 600 / 10) - 1)
                self.y_food = 10 * (random.randint(0, 480 / 10) - 1)


Game().play()
