class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 12:06.

        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)

        if s1_len + s2_len != s3_len:
            return False
        else:
            for i in range(s3_len):
                s1_idx = 0
                s2_idx = 0
                print(s3[i])
                if s1_idx < s1_len:
                    if s1[s1_idx] == s3[i]:
                        s1_idx += 1
                    elif s2_idx < s2_len:
                        if s2[s2_idx] == s3[i]:
                            s2_idx += 1
                        else:
                            return False
                elif s2_idx < s2_len:
                    if s2[s2_idx] == s3[i]:
                        s2_idx += 1
                    else:
                        return False
        
        return True


qwe = Solution()
print(qwe.isInterleave("aabcc", "dbbca" , "aadbbcbcac"))
