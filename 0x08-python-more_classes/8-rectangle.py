#!/usr/bin/python3
"""Defines  a rectangle class"""


class Rectangle:
    """Represents a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes/creates a new Rectangle
    Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
            """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the printable representation of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return ''
        symbol = str(self.print_symbol)
        return '\n'.join([symbol * self.width] * self.height)

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """ returns a printable message after every deletion"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
