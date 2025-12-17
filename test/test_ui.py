import pytest
from unittest.mock import patch, MagicMock
import pygame
from UI.ui_snake import Game_UI
from logic.snake import Direction


@pytest.fixture
def ui_instance():
    """Fixture que inicializa la UI para cada prueba."""
    pygame.init()
    yield Game_UI()
    pygame.quit()


def test_handle_input_all_directions(ui_instance):
    
    test_cases = [
        (pygame.K_UP, Direction.UP),
        (pygame.K_DOWN, Direction.DOWN),
        (pygame.K_LEFT, Direction.LEFT),
        (pygame.K_RIGHT, Direction.RIGHT),
    ]

    for key, expected_direction in test_cases:

        mock_keys = MagicMock()
        mock_keys.__getitem__.side_effect = lambda k: k == key

        with patch('pygame.key.get_pressed', return_value=mock_keys):
            
            if expected_direction in [Direction.UP, Direction.DOWN]:
                ui_instance.game.snake.direction = Direction.LEFT
            else:
                ui_instance.game.snake.direction = Direction.UP
            
            ui_instance._handle_input()

            assert ui_instance.game.snake.direction == expected_direction
            