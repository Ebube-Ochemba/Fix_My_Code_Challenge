#!/usr/bin/python3

"""square
define a class Square
"""


class Square():
    """A class Square"""

    def __init__(self, width, height):
        """
        Parameters:
        -----------
        width: int
        height: int
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of square """
        return (self.width * 2) + (self.width * 2)

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
# step 3: remove *arg and **kwargs - it's a class not a function
# step 4: pycodestyle checks
