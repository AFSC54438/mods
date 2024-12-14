class Stack:
    """simple implementation of a stack cuz why not"""

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def remove(self):
        self.stack.pop()


class Queue:
    """simple implementation of a queue cuz why not"""

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)
