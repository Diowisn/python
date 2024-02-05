import turtle

def draw_heart():
    turtle.color('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()

def main():
    turtle.speed(2)
    turtle.bgcolor('black')
    draw_heart()
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
