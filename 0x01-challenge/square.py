#!/usr/bin/python3

"""square
Define a class Square
"""


class Square():
    """Define a class Square
    ...

    Attributes
    ----------
        width : int
        height : int

    Methods
    -------
        area_of_my_square()
            Calculates the area of the square
        permiter_of_my_square()
            Calculates the perimeter of the square
        str()
            Prints a string representation of the square
    """

    width = 0
    heigth = 0

    def __init__(self, *args, **kwargs):
        """Initialize an instance of class
        Parameters
        ----------
        width : int
        height : int
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """ Perimeter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Description of square: string representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())


# step 1: class - Square, not square
# step 2: Add docs where necessary
# step 3: snake_case naming convention
# step 4: correct perimeter calculation perimeter
# step 5: pycodestyle checks
