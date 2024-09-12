"""Drawing a house with a turtle. Interesting note: In my recursion function, I made an algorithm that calculates the turn angle based on the number of sides of a shape. This only works if the shape is equal on all sides, but still cool in my opinon. I also was able to create a circle function by using small lines that slowly tilt to the right until you get a full circle."""

__author__ = "730676554"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """Start of construction of my house."""
    bart: Turtle = Turtle()
    bart.speed(10)  # Changes speed

    bart.color(88, 69, 87)
    bart.begin_fill()
    square(bart, -200.0, 0.0, 400.0)  # Draws the main square for the house.
    bart.end_fill()
    
    bart.color(78, 151, 157)
    bart.begin_fill()
    equal_triangle(bart, -200.0, 0.0, 400.0)  # Draws the roof.
    bart.end_fill()

    bart.color(33, 77, 138)
    bart.begin_fill()
    rectangle(bart, -50.0, -250.0, 100.0, 150.0)  # Draws the door.
    bart.end_fill()

    bart.color(237, 182, 226)
    circle(bart, 0.0, 200.0, 40.0)  # Draws the attic window. 

    bart.pensize(4)  # Above & Beyond: Used pensize() function.
    bart.color("black")
    bart.fillcolor(255, 241, 139)
    bart.begin_fill()
    square(bart, -150.0, -100.0, 100.0)  # Draws regular window.
    bart.end_fill()

    bart.begin_fill()
    square(bart, 50.0, -100.0, 100.0)  # Draws regular window.
    bart.end_fill()

    done()


def square(turt: Turtle, x: float, y: float, side: float) -> None:
    """Draws a square at top left starting position (x,y) and creates same length sides."""
    reset_turtle_location(turt, x, y, 0.0)
    side_recursive_loop(0, turt, side, 4)


def rectangle(turt: Turtle, x: float, y: float, x_length: float, y_length: float) -> None:
    """Draws a rectangle using different lengths."""
    reset_turtle_location(turt, x, y, 0.0)
    count: int = 0
    while count < 4:
        if count % 2 == 0:
            turt.forward(x_length)
        else: 
            turt.forward(y_length)
        turt.right(90.0)
        count = count + 1


def equal_triangle(turt: Turtle, x: float, y: float, length: float) -> None:
    """Draws a triangle starting at point (x,y) and uses 120 degree angles."""
    reset_turtle_location(turt, x, y, 60.0)
    side_recursive_loop(0, turt, length, 3)
        

def circle(turt: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a circle using (x,y) as the starting point on the farthest left side."""
    reset_turtle_location(turt, x, y, 0.0)
    side_recursive_loop(0, turt, (2 * radius * 3.14) / 360, 360)
    

def side_recursive_loop(n: int, turt: Turtle, length: float, sides: int) -> None:
    """Loops "n" times using recursion and calculates the angle needed based on the sides. ONLY WORKS FOR EQUAL SIDE LENGTHS!"""
    if n == sides:
        return None
    else:
        turt.forward(length)
        turt.right(360 / sides)
        side_recursive_loop(n + 1, turt, length, sides)


def reset_turtle_location(turt: Turtle, x: float, y: float, heading: float) -> None:
    """Places turtle at (x,y) and sets direction to face. Reduces complexity of functions."""
    turt.penup()
    turt.goto(x, y)
    turt.setheading(heading)
    turt.pendown()


if __name__ == "__main__":  
    main()