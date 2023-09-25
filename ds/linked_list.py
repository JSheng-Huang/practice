# Linked List(230912): https://p61402.github.io/2017/09/02/%E9%80%A3%E7%B5%90%E4%B8%B2%E5%88%97-Linked-List/
# 

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
        # Assert input is a node.
        if not isinstance(node, ListNode):
            node = ListNode(node)

        # If linked list is empty.
        if self.head == None:
            self.head = node
        # or append the new node to tail.
        else:
            self.tail.next = node

        # tail points to the new mode.
        self.tail = node
        self.cnt += 1

        return

    def insert(self, idx, data):
        # If the location is the end of linked list, it means appended.
        if idx == self.cnt:
            self.add(data)
        elif idx > self.cnt:
            return print("Out of bound!")
        # In bound and not the end.
        else:
            node = self.head
            inserted_node = ListNode(data)

            if idx == 0:
                inserted_node.next = node
                self.head = inserted_node
            else:
                tmp = 0

                while tmp != idx - 1:
                    node = node.next
                    tmp += 1

                inserted_node.next = node.next
                node.next = inserted_node

    def delete(self, data):
        prev = None
        node = self.head

        while node:
            if node.data == data:
                if prev:
                    prev.next = node.next
                    node = node.next
                else:
                    self.head = node.next
                    node = node.next
            else:
                prev = node
                node = node.next


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
    linked_list.insert(0, -1)
    linked_list.printLinkedList()
    linked_list.insert(0, -1)
    linked_list.printLinkedList()
    linked_list.insert(1, -10)
    linked_list.printLinkedList()
    linked_list.insert(2, -20)
    linked_list.printLinkedList()

    linked_list.delete(-1)
    linked_list.printLinkedList()
