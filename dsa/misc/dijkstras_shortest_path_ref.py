"""
# # Refer to: 
# # 1. https://blog.csdn.net/feriman/article/details/113619939
Created by JSheng <jasonhuang0124@gmail.com>"""


class Dijkstra():
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.open_list = {start: 0.0}
        self.closed_list = {}
        self.parent = {start: None}
        self.min_dis = None

    def find_shortest_path(self):
        while True:
            if self.open_list is None:
                print('ERROR!')
                break
            distance, min_node = min(
                zip(self.open_list.values(), self.open_list.keys()))
            print(min(zip(self.open_list.values(), self.open_list.keys())))
            self.open_list.pop(min_node)
            self.closed_list[min_node] = distance
            if min_node == self.goal:
                self.min_dis = distance
                shortest_path = [self.goal]
                father_node = self.parent[self.goal]
                while father_node != self.start:
                    shortest_path.append(father_node)
                    father_node = self.parent[father_node]
                shortest_path.append(self.start)
                print(shortest_path[::-1])
                print(self.min_dis)
                return
            for node in self.graph[min_node].keys():
                if node not in self.closed_list.keys():
                    if node in self.open_list.keys():
                        if self.graph[min_node][node] + distance < self.open_list[node]:
                            self.open_list[node] = distance + \
                                self.graph[min_node][node]
                            self.parent[node] = min_node
                    else:
                        self.open_list[node] = distance + \
                            self.graph[min_node][node]
                        self.parent[node] = min_node


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
