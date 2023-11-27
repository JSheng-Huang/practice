"""Floyd Warshall Algorithm
Refer to: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
Time Complexity: O(V^3), "V = Vertex".
Created by JSheng <jasonhuang0124@gmail.com>"""


def floydWarshall(graph):
    """floydWarshall()
    Consider all vertices one by one should be added into the shortest path 
    from A to B or not.
    """
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    graph_len = len(dist)

    """Add all vertices one by one to the set of intermediate vertices."""
    for k in range(graph_len):
        """Pick all vertices as source one by one."""
        for i in range(graph_len):
            """Pick all vertices as destination for the above picked source."""
            for j in range(graph_len):
                """
                If vertex k is on the shortest path from `i` to `j`, then 
                update the value of `dist[i][j]`.
                """
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    for i in range(graph_len):
        print(dist[i])


if __name__ == "__main__":
    INF = float('inf')
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    floydWarshall(graph)
