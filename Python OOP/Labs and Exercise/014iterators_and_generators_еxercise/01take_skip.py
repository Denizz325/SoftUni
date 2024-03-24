class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count - 1 == self.iterations:
            raise StopIteration

        self.iterations += 1

        return self.iterations * self.step


