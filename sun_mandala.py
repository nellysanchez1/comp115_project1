import turtle

wn = turtle.Screen()
wn.bgcolor('black')
t = turtle.Turtle()
t.speed(70)

def draw_circle():
    circle = [80]
    colors = ["red", "darkorange"]
    t.pensize(3)

    for radius in circle:
        for _ in range(9):
            for color in colors:
                t.color(color)
                t.circle(radius)
                t.right(20)

def draw_outersun():
    flower = [60,120]
    colors = ["gold","orange"]
    t.pensize(2)


    for radius in flower:
        for _ in range(9):
            for color in colors:
                t.color(color)
                t.circle(230, 60)
                t.left(120)
                t.circle(230, 60)
                t.left(120)
                t.left(10)  

def draw_sunray():
    t.pensize(1)
    for _ in range(36):
        t.color("lightyellow")
        for _ in range(3):
            t.forward(260)
            t.right(120)
        t.right(10)


draw_circle()
draw_sunray()
draw_outersun()




t.hideturtle()
wn.exitonclick()

