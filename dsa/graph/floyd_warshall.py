"""Floyd Warshall Algorithm
# # Refer to: 
# # 1. https://www.techiedelight.com/zh-tw/pairs-shortest-paths-floyd-warshall-algorithm/
# # Time Complexity: ???
Created by JSheng <jasonhuang0124@gmail.com>"""


# 遞歸的函數從源頂點`v`打印給定頂點`u`的路徑
def print_path(path, v, u, route):
    if path[v][u] == v:
        return
    print_path(path, v, path[v][u], route)
    route.append(path[v][u])


# 用路徑打印最短成本的功能
# 所有頂點對之間的#信息
def print_solution(path, n):
    for v in range(n):
        for u in range(n):
            if u != v and path[v][u] != -1:
                route = [v]
                print_path(path, v, u, route)
                route.append(u)
                print(f'The shortest path from {v} —> {u} is', route)


# 運行 Floyd–Warshall 算法的函數
def floyd_warshall(adjMatrix):

    # 基礎案例
    if not adjMatrix:
        return

    # `adjMatrix` 中的頂點總數
    n = len(adjMatrix)

    # 成本和路徑矩陣存儲最短路徑
    # (最短成本/最短路徑)信息

    # 最初，成本將與邊緣的重量相同
    cost = adjMatrix.copy()
    path = [[None for x in range(n)] for y in range(n)]

    # 初始化成本和路徑
    for v in range(n):
        for u in range(n):
            if v == u:
                path[v][u] = 0
            elif cost[v][u] != float('inf'):
                path[v][u] = v
            else:
                path[v][u] = -1

    # 運行弗洛伊德-沃歇爾
    for k in range(n):
        for v in range(n):
            for u in range(n):
                # 如果頂點 `k` 在從 `v` 到 `u` 的最短路徑上，
                # 然後更新 cost[v][u] 和 path[v][u] 的值
                if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
                        and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]

            # 如果對角元素變為負數，則
            # 圖包含負權循環
            if cost[v][v] < 0:
                print('Negative-weight cycle found')
                return

    # 打印所有頂點對之間的最短路徑
    print_solution(path, n)


if __name__ == '__main__':
    inf = float('inf')
    adjMatrix = [
        [0, inf, -2, inf],
        [4, 0, 3, inf],
        [inf, inf, 0, 2],
        [inf, -1, inf, 0]
    ]
    floyd_warshall(adjMatrix)
