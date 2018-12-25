# [Assignment 9] Vinayak Sahal vs9736

import turtle

# 1


def reverse_string(str):
    # base case to see if any values in str
    if len(str) == 0:
        return ''
    else:
        # calls the recursive function
        return reverse_string(str[1:]) + str[0]

# 2


def h_tree(order, center, size):
    # to check if the tree can be made and returns None
    if order < 0:
        return None

    # to center the tree if the coordinates have changed
    if center is not None:
        turtle.penup()
        turtle.goto(center)
        turtle.pendown()

    # makes the upper right side
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.right(90)

    # calls it here to run one part of the H-tree
    h_tree(order - 1, None, size / 2)

    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)

    # calls it here to run one part of the H-tree
    h_tree(order - 1, None, size / 2)

    turtle.left(90)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.left(90)

    # calls it here to run one part of the H-tree
    h_tree(order - 1, None, size / 2)

    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)

    # calls it here to run one part of the H-tree
    h_tree(order - 1, None, size / 2)

    turtle.left(90)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(size / 2)


# 3

def drawStar():
    # setting turtle speed and color
    turtle.speed(0)
    turtle.fillcolor('dark orange')
    turtle.begin_fill()

    # making one star in the function
    for i in range(5):
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right((360 / 5) - 120)
    turtle.end_fill()


def animate(x, y):
    # setting tracer to 0
    turtle.tracer(0)

    # infinite while loop so star spins
    while True:
        turtle.clear()
        turtle.hideturtle()
        # calling drawStar function
        drawStar()
        turtle.right(3)
        turtle.update()

# provided main function


def main():

    # Q1 - call the recursive reverse_string() function
    print(reverse_string("desserts"))
    print(reverse_string("flow"))
    print(reverse_string("abcdefg"))

    # Q2 - call the recursive H-Tree fractal function
    turtle.speed(0)
    turtle.hideturtle()
    h_tree(2, [0, 0], 300)

    # Q3 - when the mouse is clicked in the turtle window,
    # call the animate() function to display a spinning star
    turtle.onscreenclick(animate)

    turtle.done()


if __name__ == '__main__':
    main()
