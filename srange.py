#  srange means slow range :)
"""
This is the analog of python range() built-in class
It works as original except slice. For example range(100)[5:10:2] should return a range(5, 10).
My variant returns a list [5 - 9]
"""


class srange:
    """
    srange can take one, two, or three arguments. srange(start, stop, step) -> srange object.
    For example: srange(5) produces 0, 1, 2, 3, 4. These are exactly the valid indices for a list of 5 elements.
    """
    def __init__(self, start, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise ValueError("srange step argument must not be zero")
        if self.stop is None:
            self.stop = self.start
            self.start = 0

    def __len__(self):
        self.arr = [i for i in self]
        return len(self.arr)

    def __getitem__(self, item):
        self.arr = [i for i in self]
        return self.arr[item]

    def __iter__(self):
        value = self.start
        if self.step > 0:
            while value < self.stop:
                yield value
                value += self.step
        else:
            while value > self.stop:
                yield value
                value += self.step

    def __repr__(self):
        if self.stop:
            if self.step > 1:
                return "srange({}, {}, {})".format(self.start, self.stop, self.step)
        return "srange({}, {})".format(self.start, self.stop)

    def index(self, value):
        """
        srange.index(item, [start, [stop]]) -> integer. Should return index of item.
        Will raise IndexError if an item is not in srange.
        """
        counter = 0
        start = self.start
        while start < self.stop:
            if start == value:
                return counter
            start += self.step
            counter += 1
        raise IndexError("{} not in srange".format(value))

    def count(self, value):
        """
        srange.count(value) -> integer. Return 1 if value occurrences in srange and 0 if not.
        """
        return 1 if value in self else 0
