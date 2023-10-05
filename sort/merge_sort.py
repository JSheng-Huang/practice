# Refer to: https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html
#
# Created by JSheng <jasonhuang0124@gmail.com>
#

data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
# data = [10, 80, 70, 20, 30, 90, 40]


def selectionSort(array):
    for i in range(len(array)):
        tmp_min = i

        # # Select the minimum in each loop.
        for j in range(i + 1, len(array)):
            if array[j] < array[tmp_min]:
                tmp_min = j

        array[i], array[tmp_min] = array[tmp_min], array[i]

    return


if __name__ == '__main__':
    print('Default: ', data)
    selectionSort(data)
    print('Sorted: ', data)

# void merge(int array[], int left, int right, int mid)
# {
# 	int n = right - left + 1;
# 	int* x = new int[n];

# 	int i = left, j = mid + 1;
# 	for (int k=0; k<n; k++)
# 	{
# 		if      (i == mid + 1)         x[k] = array[j++];
# 		else if (j == right + 1)       x[k] = array[i++];
# 		else if (array[i] <= array[j]) x[k] = array[i++];
# 		else                           x[k] = array[j++];
# 	}

# 	for (int k=0; k<n; k++)
# 		array[left + k] = x[k];
# 	delete[] x;
# }

# void merge_sort(int array[], int left, int right)
# {
# 	if (left >= right) return;

# 	/* Divide */
# 	int mid = left + (right - left) / 2;

# 	/* Conquer */
# 	merge_sort(array, left, mid);
# 	merge_sort(array, mid+1, right);

# 	/* Combine */
# 	merge(array, left, right, mid);
# }

# void merge_sort(int array[], int n)
# {
# 	merge_sort(array, 0, n-1);
# }
