class Solution:
    def checkValidString(self, s: str) -> bool:
        # 11:38.

        if s[0] == ")":
            return False
        
        star_cnt = 0
        check_list = []

        for i in range(len(s)):
            if s[i] == "*":
                star_cnt += 1
            else:
                if s[i] == "(":
                    check_list.append("(")
                else:
                    if len(check_list) == 0:
                        if star_cnt == 0:
                            return False
                        else:
                            star_cnt -= 1
                    else:
                        check_list.pop()
        print(check_list)
        print(star_cnt)
        if len(check_list) <= star_cnt:
            return True
        else:
            return False 
            
            


qwe = Solution()
print(qwe.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
