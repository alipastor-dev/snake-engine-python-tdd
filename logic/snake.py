from enum import Enum


class Direction(Enum):

    """
    Represents the cardinal directions the snake can move.
    """
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Snake():

    """
    Manages the internal state of the snake 
   (positions, direction, and life status).
    This class is part of the Core Logic (Backend) 
    and must not be aware of Pygame.
    """

    MOVEMENT_MAP = {
        Direction.UP: (0, -1),
        Direction.DOWN: (0, 1),
        Direction.LEFT: (-1, 0),
        Direction.RIGHT: (1, 0)  
    }

    MOVEMENT_LIMITS = {
        Direction.UP: Direction.DOWN,
        Direction.DOWN: Direction.UP,
        Direction.LEFT: Direction.RIGHT,
        Direction.RIGHT: Direction.LEFT  
    }

    def __init__(self, initial_position: list[tuple[int, int]],
                 initial_direction: Direction):
        """
        Initializes the snake with its body segments and starting direction.

        Args:
        initial_position (list[tuple[int, int]]): List of (x, y) coordinates
        for he body segments.
        initial_direction (Direction): The initial movement direction.
        """
        self.body_positions = initial_position
        self.direction = initial_direction
        self.is_alive = True
        self.should_grow = False

    def check_self_collision(self):

        head = self.body_positions[0]
        return head in self.body_positions[1:]

    def move(self):
        # get the current position of head
        head_x, head_y = self.body_positions[0]

        # get the value of the coordinates for the movemente of the snake
        dx, dy = self.MOVEMENT_MAP[self.direction]

        # add the value of the coordinates to the current
        # position to make snake move
        head_x += dx
        head_y += dy

        # append the new position to the body and popout the last position
        self.body_positions.insert(0, (head_x, head_y))
        if not self.should_grow:

            self.body_positions.pop(-1)

        self.should_grow = False

        if self.check_self_collision():

            self.is_alive = False
        
    def grow(self):
        self.should_grow = True

    def change_direction(self, new_direction: Direction):

        if self.MOVEMENT_LIMITS[new_direction] != self.direction:
            self.direction = new_direction
