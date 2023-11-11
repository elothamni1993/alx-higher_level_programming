#!/usr/bin/python3
# This module defines the Rectangle class, extending from Base.

from models.base import Base

class Rectangle(Base):
    '''Class representing a rectangle shape.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes a new Rectangle instance.'''
        super().__init__(id)  # Initialize base class with id
        self.width = width  # Set rectangle width
        self.height = height  # Set rectangle height
        self.x = x  # Set x-coordinate
        self.y = y  # Set y-coordinate

    @property
    def width(self):
        '''Gets the width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width of the rectangle, ensuring it's a valid value.'''
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Gets the height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height of the rectangle, ensuring it's a valid value.'''
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''Gets the x-coordinate of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Sets the x-coordinate of the rectangle.'''
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''Gets the y-coordinate of the rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Sets the y-coordinate of the rectangle.'''
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Validates that a given attribute value is an integer and in the expected range.'''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        '''Calculates and returns the area of the rectangle.'''
        return self.width * self.height
