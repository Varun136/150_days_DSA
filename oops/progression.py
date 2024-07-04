class Progression:
    """A base class for all types of numeric progression
    Default produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start=0):
        """Initialize the values"""

        self._step = 1
        self._start = start
        self._current = start
    
    def __next__(self):
        """Get the current element of the iterator."""

        if self._current is None:
            raise StopIteration("Progression limit reached")
        current = self._current
        self._current = self._get_next() 
        return current
    
    def _get_next(self):
        """Get the next element in the progression.
        Next element will be the sum of the step and the previous element.
        """

        return self._current + self._step
    
    def __iter__(self):
        """By convention an iterator must return itself"""

        return self
    
    def get_sum(self, n):
        """Get the sum of the first n elements.
        Sum of first n natural numbers is n(n+1)/2.
        We considered whole numbers here therefore we need the sum of first n-1 natural numbers + 0.
        """

        n-=1 # 0 is also considered for whole numbers
        return ( n*(n + 1) ) // 2 # sum of the first n natural numbers
    
    def print_progression(self, n):
        """Print the first n elements in the progression."""

        print(' '.join(str(next(self)) for _ in range(n)))
        return

class ArithemeticProgression(Progression):
    """Arithemoetic progression"""

    def __init__(self, start, step=None):
        """Initialize the start and increment value."""

        if step is None: # ArithemeticProgression(n)
            start, step = 0, start

        super().__init__(start)
        self._step = step
    
    def get_sum(self, n):
        """Override the get_sum method from the base class Progression.
        Sum of first n elements of an AP is n/2[2a + (n - 1)d].
        """

        return int( ( n/2 ) * ( 2 * self._start + ( ( n-1 ) * self._step )) ) # sum of n elements in arithemetic progression.

class GeometricProgression(Progression):
    """Geometric progression"""

    def __init__(self, start, step = None):
        """Initialize start and step value."""
        
        if start == 0:
            raise ValueError("Geometric progression may never begin with 0")
        if step is None:
            start, step = 1, start
        
        super().__init__(start)
        self._step = step

    def _get_next(self):
        """Override the get_next method from base class Progression.
        Next element will be the product of the previous element and the step.
        """

        return self._current * self._step
    
    def get_sum(self, n):
        """Override the get_sum method from the base class Progression.
        Sum of first n elements for a GP is Sn = a(1 - r**n) / (1 - r).
        """

        if n == 1:
            return self._start
        
        return int( self._start * ( 1 - self._step ** n) / ( 1 - self._step ) )


class FibonacciProgression(Progression):
    """Fibonacci progression."""

    def __init__(self, start_1, start_2):
        super().__init__(start_1)
        self._step = start_2
    
    def __next__(self):
        """Get the next element in the progression.
        Next element is the sum of the previous two elements.
        """

        if self._current is None:
            raise StopIteration("Progression limit reached")

        current = self._current
        self._current, self._step = self._step, self._get_next()
        return current
    
    def get_sum(self, n):
        """Override the get_sum method from the base class Progression.
        Sum of first n elements for a Fib series is Sn = F(n+2) - 1
        """

        return self.__fib(n+1) - 1

    def __fib(self, n): # Private method.
        """ Get the n th fib number"""

        if n <= 1:
            return n

        cur, prev = 1, 0
        count = 1
        while count != n:
            cur, prev = cur + prev, cur
            count += 1
        
        return cur



if __name__ == "__main__":
    # Unit testing.
    
    p = Progression()
    p.print_progression(5)
    print(p.get_sum(2))

    k = ArithemeticProgression(5)
    k.print_progression(5)
    print(k.get_sum(2))

    l = GeometricProgression(1, 5)
    l.print_progression(5)
    print(l.get_sum(2))

    m = FibonacciProgression(0, 1)
    m.print_progression(11)
    print(m.get_sum(100))