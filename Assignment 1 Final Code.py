import turtle

X_MAX = 400
Y_MAX = 400

turtle.screensize(X_MAX , Y_MAX)

turtle.tracer(0)

background = input("Background color: ")

turtle.bgcolor(background)

def draw_shape(shape,color_code,x,y,length,height=0):

    if shape =="t":
        if height <=400:
            turtle.up()
            turtle.fillcolor(color_code)
            turtle.goto(x,y)
            turtle.begin_fill()
            turtle.down()
            turtle.forward(height)
            turtle.left(120)
            turtle.forward(height)
            turtle.left(120)
            turtle.forward(height)
            turtle.left(120)
            turtle.end_fill()

        else:
            print("out of range")

    elif shape == "r":
        if y + height <=400 and x + length <= 400:
            turtle.up()
            turtle.goto(x,y)
            turtle.fillcolor(color_code)
            turtle.begin_fill()
            turtle.down()
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
            turtle.end_fill()
            turtle.up()
            turtle.goto(0,400)

        else:
            print("out of range")
        
    elif shape =="c":
        if height <=400:
            turtle.up()
            turtle.goto(x,y)
            turtle.left(180)
            turtle.fillcolor(color_code)
            turtle.begin_fill()
            turtle.forward(height)
            turtle.down()
            turtle.circle(length)
            turtle.end_fill()
            turtle.up()
            turtle.goto(0,400)
            turtle.left(180)
        
        else:
            print("out of range")
    


def function():
    trial = []
    trynum= 2
    while trynum>= 0:

        print("triangle = t")
        print("rectangle = r")
        print("circle = c")

        user_shape = input("shape (t,r,c): ")
        color = input("color: ")
        x = int(input("x coordinate: "))
        y = int(input("y coordinate: "))
        length = int(input("length: "))
        height = int(input("height: "))
        draw_shape(user_shape, color, x, y, length, height)

        if user_shape in trial:
            print("try a different shape")
            break
        
        elif color in trial:
            print("try a different color")
            function()
        
        elif x in trial and y in trial:
            print("your shapes are going to overlap, try different coordinates")
            function()

        else: 
            return 0

function()

def enter():
    keepopen = input("Press ENTER to continue: ")
    print(keepopen)

enter()
function()