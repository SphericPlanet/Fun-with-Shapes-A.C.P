import turtle

turtle.title("Polygons on Canvas")
screen = turtle.Screen()
screen.bgcolor("Cyan")

t = turtle.Turtle()
t.pencolor("Green")
t.shape("turtle")
t.pensize(5)
t.speed(1)

def draw_triangle(side_length):
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    
def draw_rectangle(width, height):
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    
def draw_hexagon(side_length):
    t.forward(side_length)
    t.left(60)
    t.forward(side_length)
    t.left(60)
    t.forward(side_length)
    t.left(60)
    t.forward(side_length)
    t.left(60)
    t.forward(side_length)
    t.left(60)
    t.forward(side_length)

t.penup()
t.goto(-200, 100)
t.pendown()
t.fillcolor("LightGreen")
t.begin_fill()
draw_triangle(100)
t.end_fill()

t.penup()
t.goto(50, 100)
t.pendown()
t.fillcolor("LightBlue")
t.begin_fill()
draw_rectangle(150, 80)
t.end_fill()

t.penup()
t.goto(-50, -150)
t.pendown()
t.fillcolor("LightCoral")
t.begin_fill()
draw_hexagon(70)
t.end_fill()

t.hideturtle()
turtle.done()
