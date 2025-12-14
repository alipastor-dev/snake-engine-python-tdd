from logic.snake import Snake, Direction


def test_move_rigth():
    direction = Direction.RIGHT
    initial_positions = [(3, 1), (2, 1), (1, 1)]
    expected_positions = [(4, 1), (3, 1), (2, 1)]

    snake = Snake(initial_positions, direction)
    snake.move()
    assert snake.body_positions == expected_positions


def test_move_up():
    direction = Direction.UP
    initial_positions = [(3, 1), (2, 1), (1, 1)]
    expected_positions = [(3, 0), (3, 1), (2, 1)]

    snake = Snake(initial_positions, direction)
    snake.move()
    assert snake.body_positions == expected_positions


def test_move_left():
    direction = Direction.LEFT
    initial_positions = [(3, 1), (2, 1), (1, 1)]
    expected_positions = [(2, 1), (3, 1), (2, 1)]

    snake = Snake(initial_positions, direction)
    snake.move()
    assert snake.body_positions == expected_positions


def test_move_down():

    direction = Direction.DOWN
    initial_positions = [(3, 1), (2, 1), (1, 1)]
    expected_positions = [(3, 2), (3, 1), (2, 1)]

    snake = Snake(initial_positions, direction)
    snake.move()
    assert snake.body_positions == expected_positions


def test_grow_and_move():
    direction = Direction.RIGHT
    initial_positions = [(3, 1), (2, 1), (1, 1)]
    expected_body = [(5, 1), (4, 1), (3, 1), (2, 1)]
    snake = Snake(initial_positions, direction)
    snake.move()
    snake.grow()
    snake.move()
    assert snake.body_positions == expected_body