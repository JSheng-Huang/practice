# Linked List(230912)

class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.cnt = 0
        return

    def printLinkedList(self):
        if self.head == None:
            return print('You have to add nodes in the linked list first!')

        node = self.head

        while node:
            arrow = ' => ' if node.next != None else '\n'
            print(node.data, end=arrow)
            node = node.next

        return

    def add(self, node):
        if not isinstance(node, ListNode):
            node = ListNode(node)

        if self.head == None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self.cnt += 1

        return

    def insert(self, idx, data):
        if idx == self.cnt:
            self.add(data)
        elif idx > self.cnt:
            return print("Out of bound!")
        else:
            tmp = 0
            node = self.head

            while tmp != idx:
                node = node.next
                tmp += 1

            # change?
            self.add(data)


if __name__ == '__main__':
    linked_list = SingleLinkedList()

    node1 = ListNode(0)

    linked_list.printLinkedList()

    linked_list.add(node1)
    linked_list.printLinkedList()

    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.printLinkedList()

    linked_list.insert(4, 4)
    linked_list.printLinkedList()
    linked_list.insert(10000, 5)
    linked_list.printLinkedList()
    linked_list.insert(1, -1)
    linked_list.printLinkedList()
