"""
# # Refer to: 
# # 1. https://blog.csdn.net/zjjaibc/article/details/125110128  
# # 2. https://youtu.be/oLtvUWpAnTQ
Created by JSheng <jasonhuang0124@gmail.com>"""


graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"],
}


def BFS(graph, bgn):
    queue = []
    queue.append(bgn)
    seen = set()
    seen.add(bgn)
    while len(queue) > 0:
        node = queue.pop(0)
        node_neighbor = graph[node]
        for n in node_neighbor:
            if n not in seen:
                queue.append(n)
                seen.add(n)
        print(node)


def DFS(graph, bgn):
    stack = []
    stack.append(bgn)
    seen = set()
    seen.add(bgn)
    while len(stack) > 0:
        node = stack.pop()
        node_neighbor = graph[node]
        for n in node_neighbor:
            if n not in seen:
                stack.append(n)
                seen.add(n)
        print(node)


if __name__ == '__main__':
    BFS(graph, 'A')
    print('===')
    DFS(graph, 'A')
