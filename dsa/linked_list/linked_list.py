"""Linked List
Refer to: 
    1. https://p61402.github.io/2017/09/02/%E9%80%A3%E7%B5%90%E4%B8%B2%E5%88%97-Linked-List/
    2. https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/
Time Complexity: O(n), where n is the number of nodes in the linked list. 
Space Complexity: O(1) as it uses constant extra space.
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
                self.cnt += 1
        return

    def insertSorted(self, node):
        if not isinstance(node, ListNode):
            node = ListNode(node)
        if self.head == None:
            self.head = node
        elif self.head.data > node.data:
            node.next = self.head
            self.head = node
        else:
            cur_node = self.head
            while cur_node.next is not None and cur_node.next.data < node.data:
                cur_node = cur_node.next
            node.next = cur_node.next
            cur_node.next = node
        self.cnt += 1
        return

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

    def reverse(self, head, k):
        if head == None:
            return None
        cur_node = head
        next = None
        prev = None
        cnt = 0
        """Reverse first `k` nodes of the linked list."""
        while cur_node is not None and cnt < k:
            next = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next
            cnt += 1
        """
        `next` and `cur_node` are now pointers to (`k` + 1)th node, if it's 
        null, means numbers in the linked list are reversed entirely, or we 
        have to connect the reversed part to the un-reversed part by using 
        `head`, because `head` here is the tail of the reversed part.
        """
        if next is not None:
            """Choose either this,"""
            head.next = next
            """Or this."""
            # head.next = cur_node
        """`prev` is the new `head` of the input list."""
        return prev


if __name__ == '__main__':
    linked_list = SingleLinkedList()
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
    linked_list.insertSorted(5)
    linked_list.insertSorted(4)
    linked_list.insertSorted(6)
    linked_list.insertSorted(3)
    linked_list.insertSorted(7)
    linked_list.insertSorted(2)
    linked_list.insertSorted(8)
    linked_list.insertSorted(1)
    linked_list.insertSorted(9)
    linked_list.printLinkedList()
    linked_list.head = linked_list.reverse(linked_list.head, linked_list.cnt)
    linked_list.printLinkedList()
    linked_list.head = linked_list.reverse(linked_list.head, 5)
    linked_list.printLinkedList()
