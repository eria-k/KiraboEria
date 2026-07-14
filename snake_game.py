import pygame
import random
import math

# ======================================================
# GAME SETTINGS
# ======================================================

GRID_SIZE = 20

ROWS = 20
COLS = 20

WIDTH = COLS * GRID_SIZE
HEIGHT = ROWS * GRID_SIZE

FPS = 15

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,180,0)
DARK_GREEN = (0,120,0)
RED = (255,0,0)
GRAY = (40,40,40)

# Directions

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)


# ======================================================
# SNAKE GAME
# ======================================================

class SnakeGame:

    def __init__(self, render=True):

        self.render = render

        if render:

            pygame.init()

            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

            pygame.display.set_caption("Snake RL")

            self.clock = pygame.time.Clock()

            self.font = pygame.font.SysFont(None,28)

        self.reset()

    # --------------------------------------------------

    def reset(self):

        center_x = COLS // 2
        center_y = ROWS // 2

        self.direction = RIGHT

        self.snake = [

            [center_x,center_y],

            [center_x-1,center_y],

            [center_x-2,center_y]

        ]

        self.score = 0

        self.steps = 0

        self.place_food()

        return self.get_state()

    # --------------------------------------------------

    def place_food(self):

        while True:

            x = random.randint(0,COLS-1)

            y = random.randint(0,ROWS-1)

            if [x,y] not in self.snake:

                self.food = [x,y]

                break

    # --------------------------------------------------

    def head(self):

        return self.snake[0]

    # --------------------------------------------------

    def distance_to_food(self):

        head = self.head()

        return math.sqrt(

            (head[0]-self.food[0])**2 +

            (head[1]-self.food[1])**2

        )

    # --------------------------------------------------

    def move(self, action):

        """
        Action

        0 Straight

        1 Right Turn

        2 Left Turn
        """

        directions = [

            RIGHT,

            DOWN,

            LEFT,

            UP

        ]

        current = directions.index(self.direction)

        if action == 1:

            current = (current+1)%4

        elif action == 2:

            current = (current-1)%4

        self.direction = directions[current]

        head = self.head()

        new_head = [

            head[0] + self.direction[0],

            head[1] + self.direction[1]

        ]

        return new_head

    # --------------------------------------------------

    def collision(self, point=None):

        if point is None:

            point = self.head()

        x,y = point

        if x < 0 or x >= COLS:

            return True

        if y < 0 or y >= ROWS:

            return True

        if point in self.snake[:-1]:

            return True

        return False

    # --------------------------------------------------

    def draw_grid(self):

        for x in range(0,WIDTH,GRID_SIZE):

            pygame.draw.line(

                self.screen,

                GRAY,

                (x,0),

                (x,HEIGHT)

            )

        for y in range(0,HEIGHT,GRID_SIZE):

            pygame.draw.line(

                self.screen,

                GRAY,

                (0,y),

                (WIDTH,y)

            )
                # --------------------------------------------------
    # Determine the current state
    # --------------------------------------------------

    def get_state(self):

        head = self.head()

        x = head[0]
        y = head[1]

        point_straight = [
            x + self.direction[0],
            y + self.direction[1]
        ]

        # Right turn direction
        if self.direction == RIGHT:
            right_dir = DOWN
            left_dir = UP

        elif self.direction == DOWN:
            right_dir = LEFT
            left_dir = RIGHT

        elif self.direction == LEFT:
            right_dir = UP
            left_dir = DOWN

        else:   # UP
            right_dir = RIGHT
            left_dir = LEFT

        point_right = [
            x + right_dir[0],
            y + right_dir[1]
        ]

        point_left = [
            x + left_dir[0],
            y + left_dir[1]
        ]

        state = (

            # Danger
            int(self.collision(point_straight)),
            int(self.collision(point_right)),
            int(self.collision(point_left)),

            # Current Direction
            int(self.direction == UP),
            int(self.direction == DOWN),
            int(self.direction == LEFT),
            int(self.direction == RIGHT),

            # Food Location
            int(self.food[1] < y),   # Food Up
            int(self.food[1] > y),   # Food Down
            int(self.food[0] < x),   # Food Left
            int(self.food[0] > x)    # Food Right

        )

        return state

    # --------------------------------------------------

    def step(self, action):

        self.steps += 1

        old_distance = self.distance_to_food()

        new_head = self.move(action)

        # Check collision BEFORE inserting
        if self.collision(new_head):

            return self.get_state(), -100, True, self.score

        # Move snake
        self.snake.insert(0, new_head)

        reward = -0.1
        done = False

        # Eat food
        if new_head == self.food:

            self.score += 1

            reward = 10

            self.place_food()

        else:

            self.snake.pop()

            new_distance = self.distance_to_food()

            if new_distance < old_distance:

                reward += 1

            else:

                reward -= 1

        # Prevent endless wandering
        if self.steps > 100 * len(self.snake):

            done = True
            REWARD=-10

        if self.render:

            self.render_game()

        return self.get_state(), reward, done, self.score

    # --------------------------------------------------

    def render_game(self):

        # Handle close button
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                raise SystemExit

        self.screen.fill(BLACK)

        self.draw_grid()

        # Draw Snake
        for i, segment in enumerate(self.snake):

            color = GREEN if i == 0 else DARK_GREEN

            pygame.draw.rect(

                self.screen,

                color,

                (

                    segment[0] * GRID_SIZE + 1,

                    segment[1] * GRID_SIZE + 1,

                    GRID_SIZE - 2,

                    GRID_SIZE - 2

                )

            )

        # Draw Food
        pygame.draw.rect(

            self.screen,

            RED,

            (

                self.food[0] * GRID_SIZE + 1,

                self.food[1] * GRID_SIZE + 1,

                GRID_SIZE - 2,

                GRID_SIZE - 2

            )

        )

        # Score
        text = self.font.render(

            f"Score : {self.score}",

            True,

            WHITE

        )

        self.screen.blit(text, (10, 10))

        pygame.display.flip()

        self.clock.tick(FPS)

    # --------------------------------------------------

    def close(self):

        if self.render:

            pygame.quit()