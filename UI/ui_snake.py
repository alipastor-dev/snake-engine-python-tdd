from sys import exit
import pygame
from logic.game import Game
from logic.snake import Direction
import game_config


class Game_UI():

    def __init__(self) -> None:

        self.game = Game(board_width=game_config.BOARD_WIDTH, 
                         board_height=game_config.BOARD_HEIGHT)
        self.windows_x = game_config.BOARD_WIDTH * game_config.TILE_SIZE
        self.windows_y = game_config.BOARD_HEIGHT * game_config.TILE_SIZE
        pygame.init()
        self.screen = pygame.display.set_mode((self.windows_x, 
                                               self.windows_y))
        self.clock = pygame.time.Clock()

    def start_game(self) -> None:
        while self.game.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.is_running = False

            self._handle_input()
            self.game.update_game_state()
            self._draw_elements()
            self.clock.tick(game_config.GAME_SPEED)
            pygame.display.flip()

        self._display_game_over()
        pygame.quit()
        exit()

    def _handle_input(self) -> None:
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            self.game.snake.change_direction(Direction.UP)

        elif pressed_keys[pygame.K_DOWN]:
            self.game.snake.change_direction(Direction.DOWN)

        elif pressed_keys[pygame.K_LEFT]:
            self.game.snake.change_direction(Direction.LEFT)

        elif pressed_keys[pygame.K_RIGHT]:
            self.game.snake.change_direction(Direction.RIGHT)

    def _draw_elements(self) -> None:
        food_pos_x, food_pos_y = self.game.food.position
        food_square = [(food_pos_x * game_config.TILE_SIZE),
                       (food_pos_y * game_config.TILE_SIZE),
                        game_config.TILE_SIZE, game_config.TILE_SIZE]

        self.screen.fill(pygame.Color(0, 0, 0))
        pygame.draw.rect(self.screen, pygame.Color(255, 60, 100), food_square)

        # Draw snake
        for index, tile in enumerate(self.game.snake.body_positions):
            snake_x = (tile[0] * game_config.TILE_SIZE)
            snake_y = (tile[1] * game_config.TILE_SIZE)
            snake_square = [snake_x, snake_y, game_config.TILE_SIZE, 
                            game_config.TILE_SIZE]

            if index == 0:
                pygame.draw.rect(self.screen, pygame.Color(255, 0, 0), 
                                 snake_square)
            else:
                pygame.draw.rect(self.screen, pygame.Color(255, 0, 0), 
                                 snake_square)

        # Draw score on the screen
        font = pygame.font.SysFont("arial", 50, True)
        text = f"Score: {self.game.score}"
        text_surface = font.render(text, True, pygame.Color("grey")) 
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 10)
        self.screen.blit(text_surface, text_rect)

        pygame.display.flip()

    def _display_game_over(self) -> None:
        self.screen.fill(pygame.Color(0, 0, 0))

        # Draw game_over text_screen
        font_game_over = pygame.font.SysFont("arial", 30, True)
        game_over_rect = "GAME OVER"
        text_surface_game_over = font_game_over.render(game_over_rect, True, pygame.Color("grey")) 
        texto_rect_game_over = text_surface_game_over.get_rect(center=(self.windows_x // 2, self.windows_y // 2 - 50))
        self.screen.blit(text_surface_game_over, texto_rect_game_over)

        # Draw final score
        font = pygame.font.SysFont("arial", 20, True)
        text = f"Your final score: {self.game.score}"
        score_surface = font.render(text, True, pygame.Color("grey")) 
        score_rect = score_surface.get_rect()
        score_rect.topleft = (10, 40)
        self.screen.blit(score_surface, score_rect)

        # Infinite loop waiting for any command
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    pygame.quit()
                    exit()
            pygame.display.flip()
