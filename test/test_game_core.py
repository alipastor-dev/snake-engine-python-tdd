from logic.game import Game
from logic.snake import Direction

# -------- Begin wall collission tests ----------


def test_wall_collision_right_boundary() -> None:

    board_size = 4
    game = Game(board_width=board_size, board_height=board_size)
    collided_head_position = (board_size, 1)
    game.snake.body_positions[0] = collided_head_position

    collision_detected = game.check_wall_collision()

    assert collision_detected is True


def test_wall_collision_left_boundary() -> None:

    board_size = 4
    game = Game(board_width=board_size, board_height=board_size)
    collided_head_position = (-1, 1)
    game.snake.body_positions[0] = collided_head_position

    collision_detected = game.check_wall_collision()

    assert collision_detected is True


def test_wall_collision_upper_boundary() -> None:

    board_size = 4
    game = Game(board_width=board_size, board_height=board_size)
    collided_head_position = (1, 4)
    game.snake.body_positions[0] = collided_head_position

    collision_detected = game.check_wall_collision()

    assert collision_detected is True


def test_wall_collision_below_boundary() -> None:

    board_size = 4
    game = Game(board_width=board_size, board_height=board_size)
    collided_head_position = (1, -1)
    game.snake.body_positions[0] = collided_head_position

    collision_detected = game.check_wall_collision()

    assert collision_detected is True

# -------- End ----------

# -------- Begin food collission tests ----------


def test_food_collision_triggers_grow_and_score() -> None:
    board_size = 10
    game = Game(board_width=board_size, board_height=board_size)

    initial_score = game.score 
    initial_snake_length = len(game.snake.body_positions)

    collision_pos = (5, 5)

    game.food.position = collision_pos

    game.snake.body_positions[0] = collision_pos

    collision_detected = game.check_food_collision()

    game.snake.move()

    assert collision_detected is True

    assert len(game.snake.body_positions) == initial_snake_length + 1

    assert game.score == initial_score + 1

    assert game.food.position != collision_pos

# -------- End ----------

# -------- Begin game_state tests ----------

# board boundaries collision


def game_over_by_wall() -> None:
    board_size = 5
    game = Game(board_width=board_size, board_height=board_size)

    game.snake.direction = Direction.RIGHT
    initial_pos = (board_size - 1, 1)
    game.snake.body_positions[0] = initial_pos

    assert game.is_running is True

    game.update_game_state() 

    assert game.is_running is False


def game_over_by_self_collision() -> None:
    board_size = 10
    game = Game(board_width=board_size, board_height=board_size)
    body_collisionated = [(3, 3), (3, 4), (2, 4), (2, 3)]
    game.snake.body_positions = list(body_collisionated)
    game_over_detected = game.update_game_state()
    game.snake.direction = Direction.UP
    assert game_over_detected is True
    game.update_game_state()
    assert game.is_running is False
# -------- End ----------
