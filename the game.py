
import turtle

window = turtle.Screen()
window.title("Pong")   
window.bgcolor("blue")
window.setup(width=800, height=600)     #The size of the playing window
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)           #Speed of the animation (not the actual speed)
paddle_a.shape("square")    #The shape of the paddle 
paddle_a.color("red")       #The color of the paddle     
paddle_a.shapesize(stretch_wid=5,stretch_len=1)  #The sizes will be 5 and 1 (100 , 20)
paddle_a.penup()            #Eliminates the lines
paddle_a.goto(-350, 0)      #This is where the paddle starts(left)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)   ##This is where the paddle starts(right)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3       #The speed of the ball (OX)
ball.dy = 0.3       #The speed of the ball (OY)

# Scoretable
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")      #The color of the writing
pen.penup()
pen.hideturtle()        #Hides the square
pen.goto(0, 260)        #Where the scoretable is 
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))   #Info of the score

# Movement
def paddle_a_up():
    y = paddle_a.ycor()     #The first y 
    y = y + 20              #The y is increased by 20
    paddle_a.sety(y)        #The update of the paddle 

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "w")         #Paddle A is moving up by pressing "w"
window.onkeypress(paddle_a_down, "s")       #Paddle A is moving down by pressing "s"
window.onkeypress(paddle_b_up, "Up")        #Paddle B is moving up by pressing the up arrow 
window.onkeypress(paddle_b_down, "Down")    #Paddle B is moving up by pressing down arrow

# Main game loop
while True:
    window.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:           #This is where the ball bounces
        ball.sety(290)              
        ball.dy *= -1               #Reverse the direction
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        score_a = score_a + 1        #If the ball passed the paddle B , paddle A gets a point  
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)               #The ball resets
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b = score_b + 1                 #If the ball passed the paddle A , paddle B gets a point
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)              #The ball resets
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50: #The ball bounces at the collision with the paddle 
        ball.dx *= -1 
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
    
