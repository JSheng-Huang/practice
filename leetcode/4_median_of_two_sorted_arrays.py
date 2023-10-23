"""
# # Problem:
# # There are two sorted arrays nums1 and nums2 of size m and n respectively.
# # Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
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
        """
        # # Why???
        """
        if k == 1:
            return min(nums1[nums1_bgn], nums2[nums2_bgn])
        """
        # # Why???
        """
        k_1 = min(nums1_len, k // 2)
        k_2 = k - k_1
        if nums1[nums1_bgn + k_1 - 1] < nums2[nums2_bgn + k_2 - 1]:
        if (nums1[a+k1-1]<nums2[b+k2-1])
            return FindKthSmallest(nums1,a+k1,m-k1,nums2,b,n,k-k1);
        else
            return FindKthSmallest(nums1,a,n,nums2,b+k2,n-k2,k-k2);

if __name__ == '__main__':
    qwe = Solution()
    print(qwe.findMedianSortedArrays([1, 3], [2]))
    print(qwe.findMedianSortedArrays([1, 2], [3, 4]))
