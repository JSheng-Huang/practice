class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # 11:37.
    
        n = len(customers)
        y_cnt = 0
        ans = 0

        for i in customers:
            if i == 'Y':
                y_cnt += 1
        
        tmp = y_cnt

        for i in range(n):
            if customers[i] == 'Y':
                y_cnt -= 1
                penalty = y_cnt
            else:
                penalty = n - y_cnt - 1
            print(tmp)
            print(penalty)
            print('===')
            if tmp > penalty:
                tmp = penalty
                ans = i + 1
        
        return ans


qwe = Solution()
print(qwe.bestClosingTime("YYNY"))
