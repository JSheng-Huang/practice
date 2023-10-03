# Refer to: https://blog.csdn.net/FRBeVrQbN4L/article/details/109589567
# 1. The author uses lambda function, so I modify some parts.
# 2. Add some parts to prevent out-of-range error.
#
# Created by JSheng <jasonhuang0124@gmail.com>
#

def solveMaze(m, x, y, dest_x, dest_y):
    dir_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    stack = []
    stack.append([x, y])
    while len(stack) > 0:
        cur_pos = stack[-1]
        print(cur_pos)
        if cur_pos[0] == dest_x and cur_pos[1] == dest_y:
            print('INTC Yes!')
            return stack
        for dir in dir_list:
            next_pos = [cur_pos[0] + dir[0], cur_pos[1] + dir[1]]
            if next_pos[0] < 0 or next_pos[0] > len(m) or \
               next_pos[1] < 0 or next_pos[1] > len(m[0]):
                continue
            if m[next_pos[0]][next_pos[1]] == 1:
                stack.append(next_pos)
                m[next_pos[0]][next_pos[1]] = 2
                break
        # # If `for loop` ends by `break` statement, `else` would not be
        # # executed, otherwise it would.
        else:
            m[next_pos[0]][next_pos[1]] = 2
            stack.pop()
    # # `else` of `while loop` is executed whenever the loop ends due to
    # # the condition failing, rather than being stopped by `break`.
    else:
        print('AMD Yes!')
        return False


if __name__ == '__main__':
    m = [
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 1]
    ]
    routine = solveMaze(m, 0, 0, len(m) - 1, len(m[0]) - 1)
    if routine:
        print('Routine:', routine)
