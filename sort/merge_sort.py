# Refer to: https://hackmd.io/@coherent17/Sy79MIyju
#
# Created by JSheng <jasonhuang0124@gmail.com>
#

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
# data = [10, 80, 70, 20, 30, 90, 40]


def mergeSort(array):
    if len(array) > 1:
        # find the division point
        mid = len(array)//2
        left_array = array[:mid]
        right_array = array[mid:]

        print(left_array, right_array)
        # use recursion to keep dividing
        mergeSort(left_array)
        mergeSort(right_array)

        # initialize the comparison index
        right_index = 0
        left_index = 0
        merge_index = 0

        print(left_array)
        # start comparing
        # case 1: right array compare with left array
        while right_index < len(right_array) and left_index < len(left_array):
            if right_array[right_index] < left_array[left_index]:
                array[merge_index] = right_array[right_index]
                right_index += 1
            else:
                array[merge_index] = left_array[left_index]
                left_index += 1
            merge_index += 1

        # case 2: right array compare with itself
        while right_index < len(right_array):
            array[merge_index] = right_array[right_index]
            right_index += 1
            merge_index += 1

        # case 3: left array compare with itself
        while left_index < len(left_array):
            array[merge_index] = left_array[left_index]
            left_index += 1
            merge_index += 1
    return array


if __name__ == '__main__':
    print('Default: ', data)
    mergeSort(data)
    print('Sorted: ', data)
