from LinkedListTail import *


class Queue:
    def __init__(self):
        self.queue = LinkedListTail()

    def push(self, data):
        return self.queue.add_tail(data)

    def push_head(self, data):
        return self.queue.add_head(data)

    def pop(self):
        return self.queue.remove_head()

    def head(self):
        return self.queue.show_head()
