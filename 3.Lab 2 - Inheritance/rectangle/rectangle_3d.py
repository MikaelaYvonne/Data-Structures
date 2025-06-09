
import turtle as turt

from rectangle import Rectangle

class Rectangle3D (Rectangle):
    def __init__(self, x, y, width = 10, height = 10, linecolor = "black", \
                 fillcolor = "white", depth = 5, shadowcolor = "gray"):
        """

        :param x:
        :param y:
        :param width:
        :param height:
        :param linecolor:
        :param fillcolor:
        :param depth:
        :param shadowcolor:
        """
        Rectangle.__init__(x, y, width, height, linecolor, fillcolor)






def main():
    bgcolor = "lightblue"
    win = turt.Screen()
    win.bgcolor(bgcolor)
    bob = turt.Turtle()

    # Provide x and y default values for rect1
    rect1 = Rectangle(0, 0)  # Default x=0, y=0
    rect2 = Rectangle(-100, 200, 50, 120)
    rect3 = Rectangle(300, 200, 250, 250, "red", "purple")
    rect4 = Rectangle(350, 250, 150, 150, "black", None)

    rect1.draw(bob)
    rect2.draw(bob)
    rect3.draw(bob)
    rect4.draw(bob)

    rect3.erase(bob, bgcolor)
    rect3.set_x(rect3.get_x() - 300)
    rect3.set_y(rect3.get_y() - 300)
    rect3.draw(bob)

    rect3.erase(bob, bgcolor)
    rect3.set_width(rect3.get_width() * 2)
    rect3.draw(bob)

    rect3.erase(bob, bgcolor)
    rect3.set_height(rect3.get_height() // 2)
    rect3.draw(bob)

    print("rectangle 3 line color = " + rect3.get_linecolor())
    print("rectangle 3 fill color = " + rect3.get_fillcolor())

    rect3.erase(bob, bgcolor)
    rect3.set_linecolor("blue")
    rect3.set_fillcolor("red")
    rect3.draw(bob)
    print("rectangle 3 line color = " + rect3.get_linecolor())
    print("rectangle 3 fill color = " + rect3.get_fillcolor())

    print("The area of rectangle 3 is " + str(rect3.area()))


if __name__ == "__main__":
    main()
