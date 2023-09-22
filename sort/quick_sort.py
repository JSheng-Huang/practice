# Quick Sort(230828): https://www.geeksforgeeks.org/quick-sort/

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
# data = [10, 80, 70, 20, 30, 90, 40]


def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        # If `array[j]` is less than `pivot`,
        # swap it with `array[i]`, which is the element
        # that pointed by `i`.
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swap `array[high]` which is the pivot with `array[i]`,
    # which is the element that pointed by `i`.
    array[i + 1], array[high] = array[high], array[i + 1]

    # Return the position from where partition is done,
    # it means `array[i]` is at the right position.
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pos = partition(array, low, high)

        quickSort(array, low, pos - 1)
        quickSort(array, pos + 1, high)


if __name__ == '__main__':
    print('Default: ', data)
    quickSort(data, 0, len(data) - 1)
    print('Sorted: ', data)
