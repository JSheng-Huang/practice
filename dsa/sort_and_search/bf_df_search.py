"""
Refer to: https://super9.space/archives/1562
Created by JSheng <jasonhuang0124@gmail.com>"""


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.neighbors = []

    def __repr__(self):
        return 'Node(name={})'.format(self.name)


class BFS:
    def __init__(self, start):
        self.queue = []
        self.start = start

    def traversal(self):
        self.start.visited = True
        self.queue.append(self.start)

        """
        O(V)
        """
        while self.queue:
            node = self.queue.pop(0)
            yield node

            """
            O(E)
            """
            for n in node.neighbors:
                if not n.visited:
                    n.visited = True
                    self.queue.append(n)


class DFS:
    def __init__(self, start):
        self.start = start

    def traversal(self):
        interface = self.stack()
        interface(self.start)
        return self.result

    def stack(self):
        self.result = []

        def interface(node):
            self.result.append(node)
            node.visited = True
            for n in node.neighbors:
                if not n.visited:
                    interface(n)
        return interface


"""BFS"""
print('===BFS===')
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')
node_a.neighbors = [node_b, node_c]
node_b.neighbors = [node_d, node_e]
node_c.neighbors = [node_f]
bfs = BFS(node_a)
for node in bfs.traversal():
    print(node)
"""DFS"""
print('===DFS===')
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')
node_a.neighbors = [node_b, node_c]
node_b.neighbors = [node_d, node_e]
node_c.neighbors = [node_f]
dfs = DFS(node_a)
# for node in dfs.traversal():
#     print(node)
