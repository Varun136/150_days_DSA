class Range:
    """A python class that mimics the working of range class in python"""

    def __init__(self, start, stop=None, step=1):
        """ Initialize a Range instance.
        Semantics is similar to built-in range class.
        """

        if step == 0: # if given as Range(8, 20, 0)
            raise ValueError("step cannot be none") 

        if stop is None: # if given as Range(8)
            start, stop = 0, start 

        self._start = start
        self._stop = stop
        self._step = step 
        self._length = max(0, (self._stop - self._start + self._step - 1) // self._step)
        self._current = start
    
    def __len__(self):
        """Get the total length of the instance"""

        return self._length
    
    def __getitem__(self, idx):
        """Get the element at the idx'th position"""

        if (idx < 0):
            idx += len(self)

        if (0 > idx >= self._length):
            raise ValueError("Index out of range")
        

        return self._start + (self._step * idx)
    
    def __next__(self):
        current_value = self._current
        self._current = current_value + self._step
        return current_value





if __name__ == "__main__":
    v = Range(0, 100, 5)
    print(next(v))
    print(next(v))
    print(list(v))