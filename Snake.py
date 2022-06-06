import pygame
import random


snake = None
food = None

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "right"
        self.next_direction = "right"
        self.snake_list = []
        self.on_food = False

    def draw(self, surface):
        for x, y in self.snake_list:
            pygame.draw.rect(surface, (0, 255, 0), (x, y, 10, 10))

    def move(self):
        self.direction = self.next_direction
        if self.direction == "right":
            self.x += 10
        if self.direction == "left":
            self.x -= 10
        if self.direction == "up":
            self.y -= 10
        if self.direction == "down":
            self.y += 10
        if self.x > 190:
            self.x = 0
        if self.x < 0:
            self.x = 190
        if self.y > 190:
            self.y = 0
        if self.y < 0:
            self.y = 190

        if len(self.snake_list) > 1 and not self.on_food:
            self.snake_list.pop(0)
        else:
            self.on_food = False
        self.snake_list.append([self.x, self.y])

    def change_direction(self, direction):
        if direction == "right" and self.direction != "left":
            self.next_direction = direction
        if direction == "left" and self.direction != "right":
            self.next_direction = direction
        if direction == "up" and self.direction != "down":
            self.next_direction = direction
        if direction == "down" and self.direction != "up":
            self.next_direction = direction

    def check_collision(self):
        for x, y in self.snake_list[:-1]:
            if self.x == x and self.y == y:
                return True
        return False


class Food:
    def __init__(self):
        self.x = 0
        self.y = 0

    def spawn(self):
        while [self.x, self.y] in snake.snake_list:
            self.x = round(random.randrange(0, 200 - 10) / 10) * 10
            self.y = round(random.randrange(0, 200 - 10) / 10) * 10

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, 10, 10))



def main():
    global snake, food
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    snake = Snake(250, 250)
    food = Food()
    food.spawn()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.change_direction("right")
                if event.key == pygame.K_LEFT:
                    snake.change_direction("left")
                if event.key == pygame.K_UP:
                    snake.change_direction("up")
                if event.key == pygame.K_DOWN:
                    snake.change_direction("down")

        screen.fill((0, 0, 0))
        snake.move()
        food.draw(screen)
        snake.draw(screen)

        if snake.check_collision():
            print("Game Over")
            pygame.quit()
            quit()

        if snake.x == food.x and snake.y == food.y:
            food.spawn()
            snake.on_food = True

        pygame.display.update()
        clock.tick(10)


main()