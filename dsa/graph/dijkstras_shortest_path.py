"""Dijkstras Shortest Path Algorithm
# # Refer to: 
# # 1. https://blog.csdn.net/feriman/article/details/113619939
# # Time Complexity: ???
Created by JSheng <jasonhuang0124@gmail.com>"""


class Dijkstra():
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.open_dict = {start: 0.0}
        self.closed_dict = {}
        self.parent = {start: None}
        self.min_dist = None

    def find_shortest_path(self):
        while True:
            if self.open_dict is None:
                print('[ERROR] NO WAY OUT!')
                break
            """
            # # Always pick the shortest path in `open_dict` to calculate.
            # # Variables order in `zip()` in `min()` matter, refer to
            # # https://coin028.com/python/python-min-function/
            """
            self.open_dict.keys
            min_dist, min_dist_node = min(
                zip(self.open_dict.values(), self.open_dict.keys()))
            self.open_dict.pop(min_dist_node)
            self.closed_dict[min_dist_node] = min_dist

            """
            # # Reach the goal.
            """
            if min_dist_node == self.goal:
                self.min_dist = min_dist
                shortest_path = [self.goal]
                parent_node = self.parent[self.goal]
                while parent_node != self.start:
                    shortest_path.append(parent_node)
                    parent_node = self.parent[parent_node]
                shortest_path.append(self.start)
                print(shortest_path[::-1])
                print('The length of the shortest path:', self.min_dist)
                return
            """
            # # Looping neighbors of `min_dist_node`.
            """
            for node in self.graph[min_dist_node].keys():
                """
                # # `node` in `closed_dict` has already found the shortest path.
                """
                if node not in self.closed_dict.keys():
                    """
                    # # Update the shortest path in `open_dict` if it could be 
                    # # reach from the current `min_dist_node` and the length 
                    # # is shorter.
                    """
                    if node in self.open_dict.keys():
                        if self.graph[min_dist_node][node] + min_dist < self.open_dict[node]:
                            self.open_dict[node] = min_dist + \
                                self.graph[min_dist_node][node]
                            self.parent[node] = min_dist_node
                    else:
                        self.open_dict[node] = min_dist + \
                            self.graph[min_dist_node][node]
                        self.parent[node] = min_dist_node


if __name__ == '__main__':
    graph = {'1': {'2': 2, '4': 1},
             '2': {'4': 3, '5': 11},
             '3': {'1': 4, '6': 5},
             '4': {'3': 2, '6': 8, '7': 4, '5': 2},
             '5': {'7': 6},
             '7': {'6': 1}
             }
    qwe = Dijkstra(graph, '1', '6')
    qwe.find_shortest_path()
