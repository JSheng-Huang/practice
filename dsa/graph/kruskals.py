"""Kruskals's Algorithm for Minimum Spanning Tree
Refer to: 
    1. https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
    Time Complexity: O(E * logE) or O(E * logV), where V is the number of 
        vertices and E is the number of edges in the graph.
        Refer to: https://stackoverflow.com/questions/20432801/time-complexity-of-the-kruskal-algorithm
        Explanation: Sorting of edges takes O(E * logE) time. After sorting, we 
        iterate through all edges and apply the find-union algorithm. The find 
        and union operations can take at most O(logV) time. So overall 
        complexity is O(E * logE + E * logV) time. The value of E can be at 
        most O(V^2), so O(logV) and O(logE) are the same. Therefore, the 
        overall time complexity is O(E * logE) or O(E * logV).
    Space Complexity: O(V + E), where V is the number of vertices and E is the 
        number of edges in the graph.
Created by JSheng <jasonhuang0124@gmail.com>"""


class Graph:

    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = []

    def add_edge(self, bgn, end, weight):
        self.graph.append([bgn, end, weight])

    def find(self, parent, i):
        """Find the root vertex."""
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        """Union two trees
        Attach the smaller rank tree under root of the 
        higher rank tree, if ranks are same, then make one as root and 
        increment its rank by one.
        """
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def Kruskal_MST(self):
        ans = []

        """An index variable, used for sorted edges."""
        i = 0

        """Sort all the edges in non-decreasing order of their weight."""
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.vertex):
            parent.append(node)
            rank.append(0)
        """Only need (vertices - 1) edges to connect all vertices."""
        while i < self.vertex:
            """
            Pick the smallest weight edge and increment the index for next 
            iteration.
            """
            bgn, end, weight = self.graph[i]

            """
            In the first loop, they are meaningless, because all vertices are 
            unconnected in the beginning.
            """
            parentBgn = self.find(parent, bgn)
            parentEnd = self.find(parent, end)

            """
            If including this edge doesn't cause cycle, then include it in 
            result and increment the index of result for next edge. Else 
            discard the edge.
            """
            if parentBgn != parentEnd:
                ans.append([bgn, end, weight])
                self.union(parent, rank, parentBgn, parentEnd)
            i = i + 1
        minCost = 0
        print('Edges in the constructed MST')
        for u, v, weight in ans:
            minCost += weight
            print('%d -- %d == %d' % (u, v, weight))
        print('Minimum Spanning Tree', minCost)


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    g.Kruskal_MST()
