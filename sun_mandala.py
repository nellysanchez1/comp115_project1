import turtle  #create turtle module

#General adjustments, background color, t, and speed
wn = turtle.Screen() #do general adjustments, background color, t, and speed
wn.bgcolor('black')
t = turtle.Turtle()
t.speed(70)


#Circle pattern that will work as the center of the sun 
'''function to draw inner circle
'''

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


#Draw a pattern that similuates a simpleflower that worked as the outer layer for the sun
'''second function, flower shape
'''

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


#Pattern that worked as the edge of the sun
'''Third function, using triangles to the work as rays
'''

def draw_sunray():
    t.pensize(1)
    for _ in range(36):
        t.color("lightyellow")
        for _ in range(3):
            t.forward(260)
            t.right(120)
        t.right(10)


#Order in which each pattern will be drawn
draw_circle()
draw_sunray()
draw_outersun()



t.hideturtle()
wn.exitonclick()

