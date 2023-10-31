"""LeetCode#4(Hard) Median of Two Sorted Arrays
# # Problem:
# # There are two sorted arrays nums1 and nums2 of size m and n respectively.
# # Find the median of the two sorted arrays. The overall run time complexity should be O(log(m + n)).
# # 1. https://zxi.mytechroad.com/blog/algorithms/binary-search/leetcode-4-median-of-two-sorted-arrays/
# # Time Complexity: O(log(min(n1, n2)))
# # Space Complexity: O(1)
# # 2. https://github.com/wisdompeak/LeetCode/tree/master/Priority_Queue/004.Median-of-Two-Sorted-Arrays
# # Time Complexity: ???
# # Space Complexity: ???
Created by JSheng <jasonhuang0124@gmail.com>"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        """
        # # Make sure `nums1` length is smaller than `nums2` length for the 
        # # following operation.
        """
        if nums1_len > nums2_len:
            return self.findMedianSortedArrays(nums2, nums1)
        target = int((nums1_len + nums2_len + 1) / 2)
        l = 0
        r = nums1_len

        """
        # # Do Binary Search and `l` would be the k-th smallest number in two 
        # # arrays.
        """
        while l < r:
            m1 = l + (r - l) // 2
            m2 = target - m1
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1
        """
        # # Because of the previous operation, `nums1` length is smaller than 
        # # `nums2`, set `m2` as the rest portion of `l`.
        """
        m1 = l
        m2 = target - l

        """
        # # If `m1` is equal to 0 or `m2` is equal to 0, it means that the k-th 
        # # smallest number is not in `nums1` or `nums2`. If both `m1` and `m2` # # are not equal to 0, choose the larger one as the answer.
        """
        ans1 = max(float('-inf') if m1 ==
                   0 else nums1[m1 - 1], float('-inf') if m2 == 0 else nums2[m2 - 1])
        if (nums1_len + nums2_len) % 2 == 1:
            return ans1
        """
        # # If the total length of two arrays are even, it needs to take 
        # # another one to average. If `m1` is equal to `nums1` length or `m2` 
        # # is equal to `nums2` length, it means that the k-th smallest number 
        # # is not in `nums1` or `nums2`. If the length of `nums1` and `nums2` 
        # # is not equal to 0, choose the smaller one to average.
        """
        ans2 = min(float('inf') if m1 == nums1_len else nums1[m1], float(
            'inf') if m2 == nums2_len else nums2[m2])
        return (ans1 + ans2) / 2


# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         nums1_len = len(nums1)
#         nums2_len = len(nums2)
#         if (nums1_len + nums2_len) % 2 == 1:
#             return self.findKthSmallest(nums1, 0, nums1_len, nums2, 0, nums2_len, (nums1_len + nums2_len + 1) // 2)
#         else:
#             return (self.findKthSmallest(nums1, 0, nums1_len, nums2, 0, nums2_len, (nums1_len + nums2_len) // 2) + self.findKthSmallest(nums1, 0, nums1_len, nums2, 0, nums2_len, (nums1_len + nums2_len) // 2 + 1)) / 2

#     def findKthSmallest(self, nums1, nums1_bgn, nums1_len, nums2, nums2_bgn, nums2_len, k):
#         """
#         # # Always find in the smaller one.
#         """
#         if nums1_len > nums2_len:
#             return self.findKthSmallest(nums2, nums2_bgn, nums2_len, nums1, nums1_bgn, nums1_len, k)
#         """
#         # # Because the answer is not in `nums1`,
#         # # just find it in `nums2`.
#         """
#         if nums1_len == 0:
#             return nums2[nums2_bgn + k - 1]
#         """
#         # # `k == 1` => Find the smallest one in two lists.
#         """
#         if k == 1:
#             return min(nums1[nums1_bgn], nums2[nums2_bgn])
#         """
#         # # Example:
#         # # [2, 4, 6]
#         # # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#         # # `k` == 7
#         # # `k_1` == 3
#         # # `k_2` == 4
#         # # `nums1[int(nums1_bgn + k_1 - 1)]` == 6
#         # # `nums2[int(nums2_bgn + k_2 - 1)]` == 5
#         # # Compare the (k/2)-th smallest number between `nums1` and `nums2`,
#         # # if the (k/2)-th smallest number in `nums1` is smaller than the one
#         # # in `nums2`, then the k-th smallest number would not be in the top
#         # # k/2 numbers in `nums1`, because the k-th smallest number is larger
#         # # than the (k/2)-th smallest number, and vice versa.
#         # # The maximum of `k_1` is k/2, because we always choose the smaller
#         # # list as `nums1`.
#         """
#         k_1 = min(nums1_len, k // 2)
#         k_2 = k - k_1
#         if nums1[int(nums1_bgn + k_1 - 1)] < nums2[int(nums2_bgn + k_2 - 1)]:
#             return self.findKthSmallest(nums1, nums1_bgn + k_1, nums1_len - k_1, nums2, nums2_bgn, nums2_len, k - k_1)
#         else:
#             return self.findKthSmallest(nums1, nums1_bgn, nums1_len, nums2, nums2_bgn + k_2, nums2_len - k_2, k - k_2)


if __name__ == '__main__':
    qwe = Solution()
    print(qwe.findMedianSortedArrays([1, 3], [2]))
    print(qwe.findMedianSortedArrays([1, 2], [3, 4]))
    print(qwe.findMedianSortedArrays(
        [2, 4, 6], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
    print(qwe.findMedianSortedArrays(
        [20, 40, 60], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
