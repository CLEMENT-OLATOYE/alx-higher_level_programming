@property
def size (self):
    """Get the size of the square."""
    return.self_size


@size.setter
def size(self, value):
    """set the size of the square.


    Args:
    value (init) The new size of the square.
    """
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    self._size = value
