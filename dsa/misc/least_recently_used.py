"""Least Recently Used
Refer to: https://tycoon0049.medium.com/%E6%BC%94%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97-%E4%B8%80-lru-74b5771629ce
Created by JSheng <jasonhuang0124@gmail.com>"""


class Node:
    def __init__(self, key: int, value: int, left=None, right=None):
        self.prev = left
        self.next = right
        self.key = key
        self.value = value


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addLast(self, x: Node):
        """addLast()
        Add the new node to the tail.
        """
        x.next = self.tail
        x.prev = self.tail.prev
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def remove(self, x: Node):
        """Handle the previous and the next node of the removed node."""
        x.next.prev = x.prev
        x.prev.next = x.next

        """Remove the node."""
        x.prev = None
        x.next = None
        self.size -= 1

    def removeFirst(self):
        """removeFirst()
        Remove the first node, which is the least recently used node, because 
        we would re-allocate the order of nodes when users query a node.
        """
        if self.head.next == self.tail:
            return None
        first_node = self.head.next
        self.remove(first_node)
        return first_node

    def getSize(self):
        return self.size


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.d_l_l = DoubleLinkedList()

    def getData(self, key: int) -> int:
        """getData()
        Time Complexity: O(1).
        """
        x = self.map.get(key)
        if x == None:
            return -1
        self.makeRecently(key)
        return x.value

    def putData(self, key: int, value: int) -> None:
        """putData()
        Time Complexity: O(1).
        """
        x = self.map.get(key)
        if x != None:
            self.deleteKey(key)
            self.addRecently(key, value)
            return
        if self.capacity == self.d_l_l.getSize():
            self.removeLeastRecently()
        self.addRecently(key, value)
        return

    def makeRecently(self, key: int):
        x = self.map.get(key)

        """
        Remove it from the original position, then append it to the tail, which 
        means it is the most recently used.
        """
        self.d_l_l.remove(x)
        self.d_l_l.addLast(x)

    def addRecently(self, key: int, value: int):
        x = Node(key, value)
        self.d_l_l.addLast(x)
        self.map[key] = x

    def deleteKey(self, key: int):
        """deleteKey()
        Delete the data directly regardless of the order.
        """
        x = self.map.get(key)
        self.d_l_l.remove(x)
        self.map.pop(key)

    def removeLeastRecently(self):
        """removeLeastRecently()
        Remove the first node in the double link, because it's the least 
        recently used.
        """
        first_node = self.d_l_l.removeFirst()
        self.map.pop(first_node.key)


if __name__ == '__main__':
    l_r_u = LRUCache(5)
    l_r_u.putData('q', 1)
    l_r_u.putData('w', 2)
    l_r_u.putData('e', 3)
    l_r_u.putData('a', 4)
    l_r_u.putData('s', 5)
    print(l_r_u.getData('a'))
    l_r_u.deleteKey('a')
    print(l_r_u.getData('a'))
