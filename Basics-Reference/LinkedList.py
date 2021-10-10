class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_begin(self, n):
        node = Node(n)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        self.print_linked_list()

    def insert_at_end(self, n):
        node = Node(n)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1
        self.print_linked_list()

    # gives a node and removes it from the Linked List if that valued node is not present, it gives out None

    def get_node(self, val):
        temp = self.head
        if temp.val == val:
            ans = temp
            self.head = self.head.next
            self.size -= 1
            self.print_linked_list()
            return ans
        while temp.next:
            if temp.next.val == val:
                ans = temp.next
                temp.next = temp.next.next
                self.size -= 1
                self.print_linked_list()
                return ans
            temp = temp.next
        self.print_linked_list()
        return None

    def get_size(self):
        return self.size

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(str(temp.val)+" ->")
            temp = temp.next
        print("=====================")

