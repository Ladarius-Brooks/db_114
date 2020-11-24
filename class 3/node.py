class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

def remove(head, key):
    node = head
    not_found = True
    if node.data == key:
        return node.next

        while True:
            if node:
                node = node.next
            else:
                break
            if node.data == key:
                # pass
                return head
            if node.next.data == key:
                temp = node
                node = node.next.next
                temp.next = node
                return head
    return head


if __name__=="__main__":

        llist = LinkedList()
        llist.head = Node(1)
        second = Node(2)
        third = Node(3)


        llist.head.next = second
        second.next = third

        my_node = llist.head
        while True:
            if my_node:
                print(my_node.data)
                my_node = my_node.next
            else:
                break
