#!/usr/bin/python3

"""square
define a class Square
"""


class Square():
    """
    Parameters:
        width: int
        height: int
    Methods:
        area()
        PermiterOfMySquare()
        str()
    """

    width = 0
    heigth = 0

    def __init__(self, *args, **kwargs):
        """ initialize an instance of class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Description of square: string representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())


# step 1: class - Square, not square
# step 2: Add docs where necessary
# step 3: xx
# step 4: correct perimeter calculation perimeter
# step 5: pycodestyle checks
