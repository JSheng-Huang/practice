"""Prim's Algorithm for Minimum Spanning Tree
Refer to: 
    1. https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
    Time Complexity: O(V^2)
    Space Complexity: O(V)
Created by JSheng <jasonhuang0124@gmail.com>"""


class Graph():
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0 for col in range(vertex)]
                      for row in range(vertex)]

    def print_MST(self, parent):
        print('Edge \t Weight')

        """Start from 1 because we choose the first node to start"""
        for i in range(1, self.vertex):
            print(parent[i], '-', i, '\t', self.graph[i][parent[i]])

    def pick_min_dist(self, dist, checkSet):
        """Pick the minimum key
        Find the vertex with the minimum distance value from the set of 
        vertices not yet included in the shortest path tree.
        """
        min = float('inf')
        for v in range(self.vertex):
            if dist[v] < min and checkSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def prim_MST(self):
        """`dist` is used to store the minimum distances."""
        dist = [float('inf')] * self.vertex

        """`parent` is used to store parent nodes to each child node."""
        parent = [None] * self.vertex

        """Choose the first node to start."""
        dist[0] = 0

        checkSet = [False] * self.vertex
        for _ in range(self.vertex):
            """
            Pick the minimum distance vertex from the set of vertices not yet processed.
            """
            min_idx = self.pick_min_dist(dist, checkSet)
            checkSet[min_idx] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.vertex):

                # graph[u][v] is non zero only for adjacent vertices of m
                # checkSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[min_idx][v] > 0 and checkSet[v] == False \
                        and dist[v] > self.graph[min_idx][v]:
                    dist[v] = self.graph[min_idx][v]
                    parent[v] = min_idx
        print(parent)
        self.print_MST(parent)


if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]
    g.prim_MST()
