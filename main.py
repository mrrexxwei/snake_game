# [import the Screen class from turtle model]

# [import the Snake class from snake model]

# [import the Food class from food model]

# [import the Scoreboard class from scoreboard model]

# [import time model]


# [create instance of Snake, Food, Scoreboard and Screen classes]


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.18)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        # [generate another food]

        # [extend the length of snake]

        # [update the scoreboard]


    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # [break the while loop of game]
        
        # [display the Game Over info on scoreboard]
        

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # [break the while loop of game]
        
            # [display the Game Over info on scoreboard]


screen.exitonclick()
