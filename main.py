from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()

