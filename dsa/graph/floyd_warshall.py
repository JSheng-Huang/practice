"""Floyd Warshall Algorithm
# # Refer to: 
# # 1. https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
# # Time Complexity: O(V^3), "V = Vertex".
Created by JSheng <jasonhuang0124@gmail.com>"""


def floyd_warshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    graph_len = len(dist)
    """ Add all vertices one by one 
	to the set of intermediate
	vertices.
	---> Before start of an iteration, 
	we have shortest distances
	between all pairs of vertices 
	such that the shortest
	distances consider only the 
	vertices in the set 
	{0, 1, 2, .. k-1} as intermediate vertices.
	----> After the end of a 
	iteration, vertex no. k is
	added to the set of intermediate 
	vertices and the 
	set becomes {0, 1, 2, .. k}
	"""
    for k in range(graph_len):

        # pick all vertices as source one by one
        for i in range(graph_len):

            # Pick all vertices as destination for the
            # above picked source
            for j in range(graph_len):

                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    print(dist)


if __name__ == "__main__":
    INF = float('inf')
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]
    floyd_warshall(graph)
