"""Linked List
Refer to: 
    1. https://p61402.github.io/2017/09/02/%E9%80%A3%E7%B5%90%E4%B8%B2%E5%88%97-Linked-List/
Created by JSheng <jasonhuang0124@gmail.com>"""


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
            return print('[ERROR] YOU HAVE TO ADD NODES IN THE LINKED LIST FIRST!')
        node = self.head
        while node:
            arrow = ' => ' if node.next != None else '\n'
            print(node.data, end=arrow)
            node = node.next
        return

    def add(self, node):
        """Assert input is a node."""
        if not isinstance(node, ListNode):
            node = ListNode(node)
        """If linked list is empty, or append the new node to tail."""
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        """Tail points to the new mode."""
        self.tail = node

        self.cnt += 1
        return

    def insert(self, idx, data):
        if idx == self.cnt:
            self.add(data)
        elif idx > self.cnt:
            return print('[ERROR] OUT OF BOUND!')
        else:
            node = self.head
            insertedNode = ListNode(data)
            if idx == 0:
                insertedNode.next = node
                self.head = insertedNode
            else:
                tmp = 0
                while tmp != idx - 1:
                    node = node.next
                    tmp += 1
                insertedNode.next = node.next
                node.next = insertedNode

    def insertSorted(self, data):
        if not isinstance(node, ListNode):
            node = ListNode(data)
        if self.head == None:
            self.head = node
        elif self.head.data > data:
            self.insert(0, data)
        else:
            curNode = self.head
            while curNode.next is not None and curNode.next.data < node.data:
                curNode = curNode.next

        # if idx == self.cnt:
        #     self.add(data)
        # elif idx > self.cnt:
        #     return print("Out of bound!")
        # else:
        #     node = self.head
        #     insertedNode = ListNode(data)
        #     if idx == 0:
        #         insertedNode.next = node
        #         self.head = insertedNode
        #     else:
        #         tmp = 0
        #         while tmp != idx - 1:
        #             node = node.next
        #             tmp += 1
        #         insertedNode.next = node.next
        #         node.next = insertedNode

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
    # linked_list = SingleLinkedList()
    # node1 = ListNode(0)
    # linked_list.printLinkedList()
    # linked_list.add(node1)
    # linked_list.printLinkedList()
    # linked_list.add(1)
    # linked_list.add(2)
    # linked_list.add(3)
    # linked_list.printLinkedList()
    # linked_list.insert(4, 4)
    # linked_list.printLinkedList()
    # linked_list.insert(10000, 5)
    # linked_list.printLinkedList()
    # linked_list.insert(0, -1)
    # linked_list.printLinkedList()
    # linked_list.insert(0, -1)
    # linked_list.printLinkedList()
    # linked_list.insert(1, -10)
    # linked_list.printLinkedList()
    # linked_list.insert(2, -20)
    # linked_list.printLinkedList()
    # linked_list.delete(-1)
    # linked_list.printLinkedList()
    pass
