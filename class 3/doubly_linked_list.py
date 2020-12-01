class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data)
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node
    
    def add(self, new_data):
        new_node = Node(new_data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
    def show_list(self,node):
        while(node is not None):
            print(node.data),
            last = node
            node = node.next

        print("")
        while(last is not None):
            print(last.data),
            last = last.prev

llist = LinkedList()
llist.append(4)
llist.push(2)
llist.push(1)
llist.append(8)
llist.insert_after(llist.head.next,7)
llist.show_list(llist.head)