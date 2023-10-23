"""
# # Refer to: 
# # 1. https://blog.csdn.net/feriman/article/details/113619939
Created by JSheng <jasonhuang0124@gmail.com>"""


class Dijkstra():
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.open_dict = {'start': 0.0}
        self.closed_dict = {}
        self.parent = {start: None}
        self.min_dist = None

    def find_shortest_path(self):
        min_dist_node, min_dist = self.find_min_dist_node()

    def find_min_dist_node(self):
        if self.open_dict is None:
            print('[ERROR] NO WAY OUT!')
            return
        min_node = {'tmp': float('INF')}
        for k, v in self.open_dict:
            if v < min_node['tmp']:
                min_node = {k: v}
        return k, v


if __name__ == '__main__':
    graph = {'1': {'2': 2, '4': 1},
             '2': {'4': 3, '5': 11},
             '3': {'1': 4, '6': 5},
             '4': {'3': 2, '6': 8, '7': 4, '5': 2},
             '5': {'7': 6},
             '7': {'6': 1}
             }
    qwe = Dijkstra(graph, 1, 6)
    qwe.find_shortest_path()
