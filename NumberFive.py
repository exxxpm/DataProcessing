import os

class IteratorTask:
    def __init__(self, path: str):
        """Инициализирует поля класса."""
        self.file_names = os.listdir(os.path.join('dataset', path))
        self.counter = 0
        self.limit = len(self.file_names)
        self.path = path

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter - 1])
        else:
            raise StopIteration
