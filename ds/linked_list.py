# Linked List(230912)

class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        return

    def add(self, node):
        if not isinstance(node, ListNode):
            node = ListNode(node)

        if self.head == None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        return


linked_list = SingleLinkedList()

node1 = ListNode(0)

linked_list.add(node1)
linked_list.add(1)

print(linked_list.tail.data)
