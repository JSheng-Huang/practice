#
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        prev_row = [0] * (len(s2) + 1) 
        for j in range(1, len(s2) + 1): 
            prev_row[j] = prev_row[j - 1] + ord(s2[j - 1]) 

        print(prev_row)
        print(s1)
        print(s2)
        for i in range(1, len(s1) + 1): 
            curr_row = [prev_row[0] + ord(s1[i - 1])] 
            print('===')
            print(prev_row)
            print(curr_row)
            for j in range(1, len(s2) + 1): 
                if s1[i - 1] == s2[j - 1]: 
                    curr_row.append(prev_row[j - 1]) 
                else: 
                    # print(prev_row[j] + ord(s1[i - 1]))
                    # print(curr_row[j - 1] + ord(s2[j - 1]))
                    curr_row.append(min(prev_row[j] + ord(s1[i - 1]), curr_row[j - 1] + ord(s2[j - 1])))
                print(curr_row)
            prev_row = curr_row 
        return prev_row[-1]               
        
            
            


qwe = Solution()
print(qwe.minimumDeleteSum("delete", "leet"))
print(ord('d'))
print(ord('e'))
