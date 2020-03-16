from LinkedListTail import *


class Queue:
    def __init__(self):
        self.queue = LinkedListTail()

    def push(self, data):
        return self.queue.add_tail(data)

    def pop(self):
        return self.queue.remove_head()

    def peek(self):
        return self.queue.head.data

    def head(self):
        return self.queue.show_head()

    def re_head(self, replace):
        return self.queue.replace_head(replace)
