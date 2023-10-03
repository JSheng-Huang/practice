# Refer to: https://blog.csdn.net/fuxuemingzhu/article/details/82914423
#
# Created by JSheng <jasonhuang0124@gmail.com>
#

class Solution:
    def partitionDisjoint(self, A) -> int:
        disjoint = 0
        v = A[0]
        max_so_far = v
        for i in range(len(A)):
            max_so_far = max(max_so_far, A[i])
            if A[i] < v:
                v = max_so_far
                disjoint = i
        return disjoint + 1


if __name__ == '__main__':
    qwe = Solution()
    print(qwe.partitionDisjoint([5, 0, 3, 8, 6]))
    print(qwe.partitionDisjoint([1, 1, 1, 0, 6, 2]))
