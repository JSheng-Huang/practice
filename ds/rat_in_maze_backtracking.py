# https://www.codingninjas.com/studio/online-compiler/online-python-compiler

N = 4


def checkposition(m, x, y):
    if x >= 0 and x < len(m):
        if y >= 0 and y < len(m[0]):
            if m[x][y] == 1:
                return True

    return False


def solvemaze(m, sol):

    if rat_maze_sol(m, 0, 0, sol) == False:
        return False

    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")
    return True


def rat_maze_sol(m, x, y, sol):
    print('in')
    if x == len(m) - 1 and y == len(m[0]) - 1 and m[x][y] == 1:
        sol[x][y] = 1
        return True

    if checkposition(m, x, y) == True:
        if sol[x][y] == 1:
            return False

        sol[x][y] = 1

        if rat_maze_sol(m, x + 1, y, sol):
            return True

        if rat_maze_sol(m, x, y + 1, sol) == True:
            return True

        if rat_maze_sol(m, x - 1, y, sol) == True:
            return True

        if rat_maze_sol(m, x, y - 1, sol) == True:
            return True

        sol[x][y] = 0
        return False


m = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

sol = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
# Different! https://skylinelimit.blogspot.com/2018/04/python-variable-reference.html
solu = [[0] * len(m)] * len(m[0])
Lt = [[0] * 3 for i in range(3)]

print(type(sol))
print(type(solu))
# solvemaze(m, sol)
rat_maze_sol(m, 0, 0, sol)
print('---')
rat_maze_sol(m, 0, 0, solu)
