# https://www.codesdope.com/blog/article/backtracking-to-solve-a-rat-in-a-maze-c-java-pytho/
# https://www.geeksforgeeks.org/python-program-for-rat-in-a-maze-backtracking-2/

maze = [
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0]
]


def solveMaze(maze, r, c):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        print('123')
        maze[len(maze) - 1][len(maze[0]) - 1] = 'B'
        return True

    if r >= 0 and c >= 0 and r < len(maze) - 1 and c < len(maze[0]) - 1:
        if maze[r + 1][c] != 0:
            print('123')
            solveMaze(maze, r + 1, c)
        if maze[r - 1][c] != 0:
            solveMaze(maze, r - 1, c)
        if maze[r][c + 1] != 0:
            solveMaze(maze, r, c + 1)
        if maze[r][c - 1] != 0:
            solveMaze(maze, r, c - 1)

    return False


if __name__ == '__main__':
    solveMaze(maze, 0, 0)
