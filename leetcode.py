class Solution:
    def buildArray(self, target, n: int):
        # 12:07.

        ans = ["Push"] * len(target)

        pointer = 0

        for i in range(n):
            print('===')
            print(ans)
            if target[pointer] != i + 1:
                print(i)
                ans.insert(i, "Push")
                ans.insert(i + 1, "Pop")
            else:
                pointer += 1
            if pointer == len(target):
                break

        return ans          
        
            
            


qwe = Solution()
print(qwe.buildArray([1,3,4,6,7,8], 9))
