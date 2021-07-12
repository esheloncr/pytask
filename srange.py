#  srange means slow range :)

class srange:
    def __init__(self, start, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step
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
        if self.stop > 0:
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
        counter = 0
        start = self.start
        while start < self.stop:
            if start == value:
                return counter
            start += self.step
            counter += 1
        raise IndexError("{} not in srange".format(value))

    def count(self, value):
        return 1 if value in self else 0
