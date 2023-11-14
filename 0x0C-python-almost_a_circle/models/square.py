#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    '''Class representing a square shape, inheriting from Rectangle.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor for Square.
        Initializes a square with a given size, x and y coordinates, and an optional id.
        '''
        # Call the constructor of the superclass Rectangle with size for both width and height
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Property to get the size of the square.
        Since a square's width and height are equal, we can return either.
        '''
        return self.width  # Return the width as the size of the square

    @size.setter
    def size(self, value):
        '''Setter to set the size of the square.
        Updates both the width and height of the square to the given value.
        '''
        # Update both width and height to the new size
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal helper method to update square's attributes.
        It can update id, size, x, and y coordinates of the square.
        '''
        # Update the id if provided
        if id is not None:
            self.id = id
        # Update the size if provided
        if size is not None:
            self.size = size
        # Update the x-coordinate if provided
        if x is not None:
            self.x = x
        # Update the y-coordinate if provided
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates square's attributes using positional or keyword arguments.'''
        # Update using positional arguments
        if args:
            self.__update(*args)
        # Update using keyword arguments
        else:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns a dictionary representation of the square.
        Useful for serialization or debugging.
        '''
        # Return the square's properties as a dictionary
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        '''Provides a string representation of the square's properties.'''
        # Format and return the string representation
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__, self.id, self.x, self.y, self.width)

