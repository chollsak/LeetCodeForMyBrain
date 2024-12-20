class Solution:
    def scoreOfString(self, s: str) -> int:
        summ = 0
        temp = []
        for i in range(len(s)):
            print(s[i])
            if i+1 < len(s):
                score = abs(ord(s[i])-ord(s[i+1]))
                temp.append(score)
            else:
                for j in temp:
                    summ += j
                return summ
            
        
s = Solution()
print(s.scoreOfString("zaz"))