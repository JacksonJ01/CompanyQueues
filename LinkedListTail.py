class Data:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedListTail:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        new_node = Data(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return 'New value added'
        new_node.next = self.head
        self.head = new_node
        return 'New value added'

    def add_tail(self, data):
        new_node = Data(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return 'New value added'
        self.tail.next = new_node
        self.tail = new_node
        return 'New value added'

    def remove_head(self):
        if self.head is None:
            return 'No value to remove'
        gone = self.head
        self.head = self.head.next
        return gone.data, 'removed'

    def remove_tail(self):
        if self.head is None:
            return 'No value to remove'
        gone = self.head
        previous = self.head
        while gone.next is not None:
            previous = gone
            gone = gone.next
        previous.next = None
        self.tail = previous
        return gone.data, 'removed'

    def remove(self, remove):
        if self.head is None:
            return 'No value to remove'
        if self.head.data == remove:
            self.head = self.head.next
            return remove, 'removed'
        gone = self.head
        previous = self.head
        while gone.next is not None or gone.data == remove:
            if gone.data == remove and gone.next is None:
                self.tail = previous
                previous.next = None
                return gone.data, 'removed'
            if gone.data == remove:
                previous.next = previous.next.next
                return remove, 'removed'
            previous = gone
            gone = gone.next
        return 'No value to remove'

    def search(self, seek):
        if self.head.data == seek:
            return True, f'{seek} is included'
        current = self.head
        while current.next is not None:
            if current.data == seek:
                return True, f'{seek} is included'
            current = current.next
        if current.data == seek:
            return True, f'{seek} is included'
        return False, f'{seek} not included'

    def seek(self, search):
        elements = self.display()
        for element in elements:
            if search == element:
                return True, f'{search} is included'
        return False, f'{search} not included'

    def display(self):
        elements = []
        current = self.head
        while current.next is not None:
            elements.append(current.data)
            current = current.next
        elements.append(current.data)
        return elements

    def show_ht(self):
        return f'The beginning of the List is {self.head.data} and the end is {self.tail.data}'

    def show_head(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def replace_head(self, replace):
        new = Data(replace)
        new.next = self.head.next
        self.head = new
        return

    def clear_all(self):
        self.head = None
        self.tail = None
        return 'All values removed'
