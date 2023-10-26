"""LeetCode#4(Hard) Median of Two Sorted Arrays
# # Problem:
# # There are two sorted arrays nums1 and nums2 of size m and n respectively.
# # Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# # Refer to:
# # 1. https://zxi.mytechroad.com/blog/algorithms/binary-search/leetcode-4-median-of-two-sorted-arrays/
# # 2. https://github.com/wisdompeak/LeetCode/tree/master/Priority_Queue/004.Median-of-Two-Sorted-Arrays
# # Time Complexity: ???
Created by JSheng <jasonhuang0124@gmail.com>"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if (nums1_len + nums2_len) % 2 == 1:
            return self.findKthSmallest(nums1, 0, nums1_len, nums2, 0, nums2_len, (nums1_len + nums2_len + 1) // 2)
        else:
            return (self.findKthSmallest(nums1, 0, nums1_len, nums2, 0, nums2_len, (nums1_len + nums2_len) // 2) + self.findKthSmallest(nums1, 0, nums1_len, nums2, 0, nums2_len, (nums1_len + nums2_len) // 2 + 1)) / 2

    def findKthSmallest(self, nums1, nums1_bgn, nums1_len, nums2, nums2_bgn, nums2_len, k):
        """
        # # Always find in the smaller one.
        """
        if nums1_len > nums2_len:
            return self.findKthSmallest(nums2, nums2_bgn, nums2_len, nums1, nums1_bgn, nums1_len, k)
        """
        # # Because the answer is not in `nums1`,
        # # just find it in `nums2`.
        """
        if nums1_len == 0:
            return nums2[nums2_bgn + k - 1]
        """
        # # `k == 1` => Find the smallest one in two lists.
        """
        if k == 1:
            return min(nums1[nums1_bgn], nums2[nums2_bgn])
        """
        # # Example:
        # # [2, 4, 6]
        # # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        # # `k` == 7
        # # `k_1` == 3
        # # `k_2` == 4
        # # `nums1[int(nums1_bgn + k_1 - 1)]` == 6
        # # `nums2[int(nums2_bgn + k_2 - 1)]` == 5
        # # Compare the (k/2)-th smallest number between `nums1` and `nums2`,
        # # if the (k/2)-th smallest number in `nums1` is smaller than the one
        # # in `nums2`, then the k-th smallest number would not be in the top 
        # # k/2 numbers in `nums1`, because the k-th smallest number is larger 
        # # than the (k/2)-th smallest number, and vice versa.
        # # The maximum of `k_1` is k/2, because we always choose the smaller
        # # list as `nums1`.
        """
        k_1 = min(nums1_len, k // 2)
        k_2 = k - k_1
        if nums1[int(nums1_bgn + k_1 - 1)] < nums2[int(nums2_bgn + k_2 - 1)]:
            return self.findKthSmallest(nums1, nums1_bgn + k_1, nums1_len - k_1, nums2, nums2_bgn, nums2_len, k - k_1)
        else:
            return self.findKthSmallest(nums1, nums1_bgn, nums1_len, nums2, nums2_bgn + k_2, nums2_len - k_2, k - k_2)


if __name__ == '__main__':
    qwe = Solution()
    print(qwe.findMedianSortedArrays([1, 3], [2]))
    print(qwe.findMedianSortedArrays([1, 2], [3, 4]))
    print(qwe.findMedianSortedArrays(
        [2, 4, 6], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
