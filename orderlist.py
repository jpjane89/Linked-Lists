class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.data > data:
                stop = True
            else:
                previous = current
                current = current.next

        node = Node(data)

        if current == None:
            self.head = node
            self.tail = node
        elif previous == None:
            self.head = node
            node.next = current
        else:
            previous.next = node
            node.next = current

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next

        return count

    def search (self,data):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.data == data:
                found = True
            elif current.data > data:
                stop = True
            else:
                current = current.next

        return found

    def remove(self, data):
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current == data:
                found = True
            else:
                previous = current
                current = current.next

        if previous == None:
            self.head = current.next

        else:
            previous.next = current.next

    def index(self, data):
        current = self.head
        position = 0
        found = False

        while current != None and not found:
            if current.data == data:
                found = True
            else:
                position += 1
                current = current.next
        if found:
            return position
        else:
            return "Error"

    def pop(self, pos=None):
        current = self.head
        previous = None
        position = 0
        found = False

        if pos == None:
            pos = self.size() - 1

        while current != None and not found:
            if position == pos:
                found = True
            else:
                position += 1
                previous = current
                current = current.next

        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

        return current.data

    def print_list(self):
        current = self.head

        while current != None:
            print current.data
            current = current.next