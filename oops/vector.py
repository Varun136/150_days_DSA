class Vector:
    """ 
    Represent the vector with 3 co-ordinates representing the position of the vector in 
    3-dimensional geometry.
    Supports all vector operations.
    """

    def __init__(self, dimen: int, coords: list = None):

        if coords:
            if dimen != len(coords):
                raise TypeError("invalid co-ordinate length")

        self._dimen = dimen
        self._coords = [0] * dimen if not coords else  coords
    
    def __str__(self):
        """Return the co-ordinates while printing the vector instance"""

        return "< " + str(self._coords)[1:-1] + " >"
    
    def __add__(self, vector: 'Vector') -> 'Vector':
        """Addition operator for the vector classes."""

        if not (isinstance(vector, Vector) or isinstance(vector, list)):
            raise ValueError("Both objects should belong to class \"Vector\" or should be a list of equal dimension.")
        if len(self) != len(vector):
            raise ValueError("Dimensions must be same.")

        return Vector(self._dimen, [vector[i] + self[i] for i in range(self._dimen)])
    
    def __getitem__(self, idx: int) -> int:
        """Return the co_ordinate at index idx in the vector co-ordintates"""

        if idx >= self._dimen:
            raise ValueError("Index out of range")
        return self._coords[idx]
    
    def __setitem__(self, idx, value):
        """Set the value at the index idx for the vector coordinates"""

        if idx >= self._dimen:
            raise ValueError("Index out of range")
        self._coords[idx] = value
        return True
    
    def __len__(self):
        """Get the total number of co ordinates"""

        return self._dimen

    def __eq__(self, vector):
        """Checks if the cordinates are equal"""

        return self._coords == vector._coords
    
    def __ne__(self, vector):
        """Checks if the co ordinates are not equal"""

        return not self == vector
    
    def __sub__(self, vector):
        """Subtract two vectors"""

        if len(vector) != len(self):
            raise ValueError("Dimensions must be same.")

        return Vector(self._dimen, [self[i]-vector[i] for i in range(self._dimen)])
    
    def __neg__(self):
        """Get the negative of coordinates"""

        for i in range(self._dimen):
            self._coords[i] = -self._coords[i]
        return self

    
u = Vector(5)
u[0] = 4
v = Vector(5)
v[0] = 1

print(-v)

# for i in v:
    # print("hi")