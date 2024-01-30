#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def _init(self, size=0):
        """initialize anew Square.

    Args:
    value (init) The new size of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    self._size = size
