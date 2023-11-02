"""kruskals's Algorithm for Minimum Spanning Tree
Refer to: 
    1. https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
    Time Complexity: ???
    Space Complexity: ???
Created by JSheng <jasonhuang0124@gmail.com>"""


class Graph:

    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = []

    def add_edge(self, bgn, end, weight):
        self.graph.append([bgn, end, weight])

    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(self, parent, i):
        if parent[i] != i:

            # Reassignment of node's parent
            # to root node as
            # path compression requires
            parent[i] = self.find(parent, parent[i])
        # print(parent)
        # print(parent[i])
        return parent[i]

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1

    # The main function to construct MST
    # using Kruskal's algorithm
    def Kruskal_MST(self):

        # This will store the resultant MST
        result = []

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Sort all the edges in
        # non-decreasing order of their
        # weight
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
        print(self.graph)
        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.vertex):
            parent.append(node)
            rank.append(0)
        print(parent)
        print(rank)
        # Number of edges to be taken is less than to V-1
        while e < self.vertex - 1:

            # Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                print(parent)
            # Else discard the edge

        minimumCost = 0
        print('Edges in the constructed MST')
        for u, v, weight in result:
            minimumCost += weight
            print('%d -- %d == %d' % (u, v, weight))
        print('Minimum Spanning Tree', minimumCost)


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    g.Kruskal_MST()
