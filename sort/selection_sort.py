# Selection Sort: https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html
#

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
# data = [10, 80, 70, 20, 30, 90, 40]


def selectionSort(array):
    for i in range(len(array)):
        tmp_min = i

        # Select the minimum in each loop.
        for j in range(i + 1, len(array)):
            if array[j] < array[tmp_min]:
                tmp_min = j

        array[i], array[tmp_min] = array[tmp_min], array[i]

    return


if __name__ == '__main__':
    print('Default: ', data)
    selectionSort(data)
    print('Sorted: ', data)
