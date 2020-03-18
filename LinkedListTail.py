class Data:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedListTail:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        new = Data(data)
        if self.head is None:
            self.head = new
            self.tail = new
            return new.data
        new.next = self.head
        self.head = new
        return new.data

    def remove_head(self):
        gone = self.head
        self.head = self.head.next
        return gone.data

    def add_tail(self, data):
        new = Data(data)
        if self.head is None:
            self.add_head(data)
            return new.data
        self.tail.next = new
        self.tail = new
        return new.data

    def remove_tail(self):
        tail = self.head
        gone = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
            return gone.data
        while gone.next is not None:
            tail = gone
            gone = gone.next
        tail.next = None
        self.tail = tail
        return gone.data

    def show(self):
        shows = []
        if self.head is None:
            return shows
        current = self.head
        while current.next is not None:
            shows.append(current.data)
            current = current.next
        shows.append(current.data)
        return shows

    def show_head(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def clear(self):
        self.head = None
        self.tail = None
