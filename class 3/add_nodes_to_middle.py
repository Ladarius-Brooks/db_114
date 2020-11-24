class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def get_len(head):
        node = head
        while True:
            if node:
                size += 1
                node = node.next
            else:
                break

        return size

def print_list(head):
        node = head
        while True:
            if node:
                print(node.data)
                node = node.next
            else:
                break

if __name__=="__main__":
    head = Node(1)
    node = head
    for index in range(1, 10):
        node.next = Node(index)
        node = node.next

    print("the size of my list is: %s" % get_len(head))

    node = head
    next_node = head.next
    new_mode = Node(10)
    node.next = new_node
    node.next.next = next_node

    print("the size of my list is: %s" % get_len(head))
    print_list(head)

# try to change this using the linked_list class