import turtle
import random

# Constants
SCREEN_SIZE = 600
STEP = 20
INITIAL_DELAY = 0.15

class SnakeGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Turtle Snake Game")
        self.screen.screensize(SCREEN_SIZE, SCREEN_SIZE)
        self.screen.bgcolor("yellow")
        self.screen.tracer(0)
        self.score = 0
        self.delay = INITIAL_DELAY
        self.snake = []
        self.food = self.create_food()
        self.initialize_snake()
        self.display_score()
        self.bind_controls()

    def initialize_snake(self):
        head = turtle.Turtle()
        head.shape("square")
        head.color("black")
        head.penup()
        self.snake.append(head)

    def create_food(self):
        food = turtle.Turtle()
        food.shape("circle")
        food.color("red")
        food.penup()
        food.goto(random.randint(-SCREEN_SIZE//2, SCREEN_SIZE//2),
                  random.randint(-SCREEN_SIZE//2, SCREEN_SIZE//2))
        return food

    def display_score(self):
        self.score_display = turtle.Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.goto(0, SCREEN_SIZE // 2 - 40)
        self.score_display.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
        head = self.snake[0]
        if head.direction == "up":
            head.sety(head.ycor() + STEP)
        elif head.direction == "down":
            head.sety(head.ycor() - STEP)
        elif head.direction == "left":
            head.setx(head.xcor() - STEP)
        elif head.direction == "right":
            head.setx(head.xcor() + STEP)

    def grow_snake(self):
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("gray")
        segment.penup()
        self.snake.append(segment)

    def check_collisions(self):
        head = self.snake[0]
        # Check collision with walls
        if abs(head.xcor()) > SCREEN_SIZE // 2 or abs(head.ycor()) > SCREEN_SIZE // 2:
            return True
        # Check collision with self
        for segment in self.snake[1:]:
            if segment.distance(head) < 20:
                return True
        return False

    def update_food(self):
        if self.snake[0].distance(self.food) < 20:
            self.food.goto(random.randint(-SCREEN_SIZE//2, SCREEN_SIZE//2),
                           random.randint(-SCREEN_SIZE//2, SCREEN_SIZE//2))
            self.grow_snake()
            self.score += 1
            self.score_display.clear()
            self.score_display.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
            self.delay = max(0.05, self.delay - 0.01)

    def bind_controls(self):
        self.screen.listen()
        self.screen.onkey(lambda: self.set_direction("up"), "Up")
        self.screen.onkey(lambda: self.set_direction("down"), "Down")
        self.screen.onkey(lambda: self.set_direction("left"), "Left")
        self.screen.onkey(lambda: self.set_direction("right"), "Right")

    def set_direction(self, direction):
        head_direction = self.snake[0].direction
        if (direction == "up" and head_direction != "down") or \
           (direction == "down" and head_direction != "up") or \
           (direction == "left" and head_direction != "right") or \
           (direction == "right" and head_direction != "left"):
            self.snake[0].direction = direction

    def run_game(self):
        self.snake[0].direction = "stop"
        while True:
            self.screen.update()
            self.move()
            self.update_food()
            if self.check_collisions():
                break
            self.screen.ontimer(None, int(self.delay * 1000))
        self.screen.bye()  # Close game window on game over


if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()