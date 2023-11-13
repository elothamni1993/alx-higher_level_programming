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

    def display(self):
        '''Prints string representation of this rectangle.'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''Returns a string representation of the rectangle's properties.'''
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal helper to update rectangle properties.'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates rectangle properties using either positional or keyword arguments.'''
        if args:
            self.__update(*args)
        else:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Converts the rectangle's attributes to a dictionary.'''
        return {"id": self.id, "width": self.__width, "height": self.__height, "x": self.__x, "y": self.__y}
