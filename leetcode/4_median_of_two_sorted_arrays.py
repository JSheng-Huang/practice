"""
# # Refer to: 
# # 1. https://zxi.mytechroad.com/blog/algorithms/binary-search/leetcode-4-median-of-two-sorted-arrays/
# # 2. https://github.com/wisdompeak/LeetCode/tree/master/Priority_Queue/004.Median-of-Two-Sorted-Arrays
Created by JSheng <jasonhuang0124@gmail.com>"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if (nums1_len + nums2_len) % 2 == 1:
            pass

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
        if nums1 == 0:
            return nums2_bgn + k - 1


if __name__ == '__main__':
    qwe = Solution()
    print(qwe.findMedianSortedArrays([1, 3], [2]))
    print(qwe.findMedianSortedArrays([1, 2], [3, 4]))
