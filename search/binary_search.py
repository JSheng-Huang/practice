# https://medium.com/appworks-school/binary-search-%E9%82%A3%E4%BA%9B%E8%97%8F%E5%9C%A8%E7%B4%B0%E7%AF%80%E8%A3%A1%E7%9A%84%E9%AD%94%E9%AC%BC-%E4%B8%80-%E5%9F%BA%E7%A4%8E%E4%BB%8B%E7%B4%B9-dd2cd804aee1
#

import math


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = math.floor((left + right) / 2)

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid

    return left
    # return -1


if __name__ == '__main__':
    nums = [1, 3, 5, 6, 7, 8, 9, 11, 13, 24]
    ans = binary_search(nums, 4)
    print(ans)
