from random import randint

from logic.snake import Snake, Direction
from logic.food import Food


class Game_Core():

    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.is_running = True
        self.score = 0
        self.snake = Snake([(3, 1), (2, 1), (1, 1)], Direction.RIGHT)
        self.place_food()

    def place_food(self):

        while True:
            pos_x = randint(0, self.board_width - 1)
            pos_y = randint(0, self.board_height - 1)

            new_pos = (pos_x, pos_y)

            if new_pos not in self.snake.body_positions:
                self.food = Food(new_pos)
                break

    def check_wall_collision(self):
        head = self.snake.body_positions[0]
        overpassed_x = head[0] >= self.board_width or head[0] < 0
        overpassed_y = head[1] >= self.board_height or head[1] < 0
        collide = (overpassed_x or overpassed_y)

        return collide

    def check_food_collision(self):
        food_pos = self.food.position
        head = self.snake.body_positions[0]

        if head == food_pos:
            self.snake.grow()
            self.place_food()
            self.score += 1
            return True
        else:
            return False

    def update_game_state(self):

        if not self.is_running:
            return
        self.snake.move()

        if self.check_wall_collision() or not self.snake.is_alive:
            self.is_running = False
            return
        self.check_food_collision()