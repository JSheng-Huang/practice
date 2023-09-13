# Quick Sort(230828): https://www.geeksforgeeks.org/quick-sort/

# data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
data = [10, 80, 30, 90, 40]

# Function to find the partition position


def partition(array, low, high):
    print('Partitioning: ', data)
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        print('current i: ', i)
        print('current j: ', j)
        print('pivot: ', pivot)
        print('---')
        if array[j] < pivot:
            print('array[j]: ', array[j])
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            print('i in if-else: ', i)
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            print('Looping array: ', array)
    print('===')
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    print('Functional array: ', array)
    print('final i: ', i)
    print('___')
    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


if __name__ == '__main__':
    print('Default: ', data)
    quickSort(data, 0, len(data) - 1)
    print('Sorted: ', data)
