# Author: Mikaela Yvonne Dacanay
# Date: 05/20/2025
# Description: This program creates a class fora a rectangle. It provides
# getters and setters for the class variables, a draw functions


import turtle as turt

class Rectangle:

    def __init__(self, x, y, width = 10, height = 10,  linecolor = "black", fillcolor = "white"):
        """

        :param x:
        :param y:
        :param width:
        :param height:
        :param linecolor:
        :param fillcolor:
        """

        self.__x = x
        self.__y = y
        if width < 0:
            self.__width = 0
        else:
            self.__width = width
        if height < 0:
            self.__height = 0
        else:
            self.__height = height
        self.__linecolor = linecolor
        self.__fillcolor = fillcolor


    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self,width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_linecolor(self):
        return self.__linecolor

    def set_linecolor(self, color):
        self.__linecolor = color

    def get_fillcolor(self):
        return self.__fillcolor

    def set_fillcolor(self, color):
        self.__fillcolor = color

    def area(self):
        return self.__width * self.__height

    def draw(self, turt):

        turt.penup()
        turt.goto(self.__x, self.__y)
        turt.setheading(0)
        turt.pendown()
        turt.pencolor(self.__linecolor)
        if self.__fillcolor is not None:
            turt.fillcolor(self.__fillcolor)
            turt.begin_fill()

        for i in range(2):
            turt.forward(self.__width)
            turt.right(90)
            turt.forward(self.__height)
            turt.right(90)

        if self.__fillcolor is not None:
            turt.end_fill()


    def erase(self, turt, bgcolor):
        turt.penup()
        turt.goto(self.__x, self.__y)
        turt.setheading(0)
        turt.pendown()
        turt.color(bgcolor, bgcolor)
        turt.begin_fill()
        for i in range(2):
            turt.forward(self.__width)
            turt.right(90)
            turt.forward(self.__height)
            turt.right(90)
        turt.end_fill()

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


if __name__ == "__main__":
    main()
