from sys import exit
import pygame
from logic.game import Game
from logic.snake import Direction
import game_config


class Game_UI():

    def __init__(self):

        self.game = Game(board_width=game_config.BOARD_WIDTH, 
                         board_height=game_config.BOARD_HEIGHT)
        self.windows_x = game_config.BOARD_WIDTH * game_config.TILE_SIZE
        self.windows_y = game_config.BOARD_HEIGHT * game_config.TILE_SIZE
        pygame.init()
        self.screen = pygame.display.set_mode((self.windows_x, 
                                               self.windows_y))
        self.clock = pygame.time.Clock()

    def start_game(self):
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

    def _handle_input(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            self.game.snake.change_direction(Direction.UP)
            
        elif pressed_keys[pygame.K_DOWN]:
            self.game.snake.change_direction(Direction.DOWN)
            
        elif pressed_keys[pygame.K_LEFT]:
            self.game.snake.change_direction(Direction.LEFT)
            
        elif pressed_keys[pygame.K_RIGHT]:
            self.game.snake.change_direction(Direction.RIGHT)

    def _draw_elements(self):
        food_pos_x, food_pos_y = self.game.food.position
        food_square = [(food_pos_x * game_config.TILE_SIZE),
        (food_pos_y * game_config.TILE_SIZE), game_config.TILE_SIZE, 
            game_config.TILE_SIZE]

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
             
        # draw score in the screem
        font = pygame.font.SysFont("arial", 50, True)
        text = f"Score: {self.game.score}"
        texto_surface = font.render(text, True, pygame.Color("grey")) 
        texto_rect = texto_surface.get_rect()
        texto_rect.topleft = (10, 10)
        self.screen.blit(texto_surface, texto_rect)
        
        pygame.display.flip()

    def _display_game_over(self):
        self.screen.fill(pygame.Color(0, 0, 0))

        # Draw game_over text_screen
        font_game_over = pygame.font.SysFont("arial", 30, True)
        text_game_over = "GAME OVER"
        texto_surface_game_over = font_game_over.render(text_game_over, True, pygame.Color("grey")) 
        texto_rect_game_over = texto_surface_game_over.get_rect(center=(self.windows_x // 2, self.windows_y // 2 - 50))
        self.screen.blit(texto_surface_game_over, texto_rect_game_over)

        # Draw final score
        font = pygame.font.SysFont("arial", 20, True)
        text = f"Your final score: {self.game.score}"
        texto_surface = font.render(text, True, pygame.Color("grey")) 
        texto_rect = texto_surface.get_rect()
        texto_rect.topleft = (10, 40)
        self.screen.blit(texto_surface, texto_rect)

        # Infinite loop waiting por any commamd:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    pygame.quit()
                    exit()
            pygame.display.flip()


if __name__ == "__main__":
    # Creamos la instancia de la interfaz de usuario
    ui = Game_UI()
    
    # Arrancamos el bucle principal del juego
    ui.start_game()