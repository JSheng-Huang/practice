class Solution:
    def totalSteps(self, nums) -> int:
        res = 0
        stack = []

        for num in nums:
            val = 1
            print(stack)
            while stack and stack[-1][0] <= num:
                print(num)
                val = max(val, stack.pop(-1)[1] + 1)
                print(val)
            if not stack:
                val = 0
            print(stack)
            stack.append((num, val))
            res = max(res, val)
        return res


if __name__ == '__main__':
    qwe = Solution()
    print(qwe.totalSteps([56, 4, 2, 7]))
