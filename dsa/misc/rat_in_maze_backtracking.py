# Refer to:
# https://www.codingninjas.com/studio/online-compiler/online-python-compiler
#
# Created by JSheng <jasonhuang0124@gmail.com>
#

def isValid(m, x, y):
    if x >= 0 and x < len(m):
        if y >= 0 and y < len(m[0]):
            if m[x][y] == 1:
                return True
    return False


def solveMaze(m, x, y, s):
    if x == len(m) - 1 and y == len(m[0]) - 1 and m[x][y] == 1:
        s[x][y] = 1
        return True
    if isValid(m, x, y):
        if s[x][y] == 1:
            return False
        s[x][y] = 1
        if solveMaze(m, x + 1, y, s):
            return True
        if solveMaze(m, x, y + 1, s):
            return True
        if solveMaze(m, x - 1, y, s):
            return True
        if solveMaze(m, x, y - 1, s):
            return True
        s[x][y] = 0
        return False


if __name__ == '__main__':
    m = [
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 1]
    ]

    # # (jason_huang):
    # # Both are available.
    s = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    s = [[0] * len(m) for i in range(len(m[0]))]

    # # (jason_huang):
    # # This would fail because of shallow copy:
    # # 1. https://skylinelimit.blogspot.com/2018/04/python-variable-reference.html
    # # 2. https://ithelp.ithome.com.tw/articles/10221255
    # s = [[0] * len(m)] * len(m[0])

    try:
        if solveMaze(m, 0, 0, s):
            print('INTC Yes!')
        else:
            print('AMD Yes!')
    except:
        print('[ERROR] INFINITE LOOP!')
    finally:
        print(s)
