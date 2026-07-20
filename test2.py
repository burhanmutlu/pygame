import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# --- Configuration & Constants ---
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors (RGB)
COLOR_BG = (20, 20, 20)
COLOR_SNAKE = (46, 204, 113)
COLOR_FOOD = (231, 76, 60)
COLOR_TEXT = (236, 240, 241)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 24)
        self.reset_game()

    def reset_game(self):
        """Resets the game state for a new game."""
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.score = 0
        self.spawn_food()

    def spawn_food(self):
        """Spawns food at a random position not occupied by the snake."""
        while True:
            self.food = (
                random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1)
            )
            if self.food not in self.snake:
                break

    def handle_events(self):
        """Handles keypresses and window closing."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.next_direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.next_direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.next_direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.next_direction = RIGHT

    def update(self):
        """Updates the game logic (movement, collisions)."""
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        # Collision with walls
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
                new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            self.reset_game()
            return

        # Collision with self
        if new_head in self.snake:
            self.reset_game()
            return

        # Move snake head
        self.snake.insert(0, new_head)

        # Check for food consumption
        if new_head == self.food:
            self.score += 10
            self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()

    def draw(self):
        """Renders the game elements onto the screen."""
        self.screen.fill(COLOR_BG)

        # Draw Snake
        for block in self.snake:
            rect = pygame.Rect(block[0] * GRID_SIZE, block[1] * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2)
            pygame.draw.rect(self.screen, COLOR_SNAKE, rect)

        # Draw Food
        food_rect = pygame.Rect(self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2)
        pygame.draw.rect(self.screen, COLOR_FOOD, food_rect)

        # Draw Score
        score_text = self.font.render(f"Score: {self.score}", True, COLOR_TEXT)
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()

    def run(self):
        """Main game loop."""
        while True:
            self.handle_events()
            self.update()
            self.draw()
            # Set the game speed (FPS)
            self.clock.tick(10 + len(self.snake) // 5)  # Slightly speeds up as you grow


if __name__ == "__main__":
    game = SnakeGame()
    game.run()