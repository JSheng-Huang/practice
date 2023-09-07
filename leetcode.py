class Solution:
    def tupleSameProduct(self, nums) -> int:
        ans = 0
        freq = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                key = nums[i] * nums[j]
                print(freq.get(key, 0))
                ans += freq.get(key, 0)
                # print(ans)
                freq[key] = 1 + freq.get(key, 0)
        print(freq)
        return 8*ans
            
            


qwe = Solution()
print(qwe.tupleSameProduct([1,2,4,5,10]))
