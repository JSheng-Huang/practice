# Selection Sort: https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html
#

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
# data = [10, 80, 70, 20, 30, 90, 40]


def selectionSort(array):
    for i in range(len(array)):
        min_idx = i

        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]


if __name__ == '__main__':
    print('Default: ', data)
    selectionSort(data)
    print('Sorted: ', data)
