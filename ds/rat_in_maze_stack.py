# https://blog.csdn.net/FRBeVrQbN4L/article/details/109589567

def solveMaze(m, x, y, dest_x, dest_y):
    # The author uses lambda function, modify it...
    dir_list = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    stack = []
    stack.append((x, y))

    while len(stack) > 0:
        cur_pos = stack[-1]

        if cur_pos[0] == dest_x and cur_pos[1] == dest_y:
            print('INTC Yes!')
            for i in stack:
                print(i)
            return True

        # The author uses lambda function, modify it...
        for dir in dir_list:
            next_pos = dir(cur_pos[0], cur_pos[1])
            if m[next_pos[0]][next_pos[1]] == 0:
                stack.append(next_pos)
                m[next_pos[0]][next_pos[1]] = 2
                break
        else:
            m[next_pos[0]][next_pos[1]] = 2
            stack.pop()
    else:
        print('AMD Yes!')
        return False


if __name__ == '__main__':
    m = [
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 1]
    ]

    solveMaze(m, 0, 0, 3, 3)
