class reverse_iter:
    def __init__(self, some_iter):
        self.some_iter = some_iter
        self.current_index = len(self.some_iter)

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index -= 1
        if self.current_index >= 0:
            return self.some_iter[self.current_index]
        raise StopIteration
