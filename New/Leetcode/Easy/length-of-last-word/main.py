class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        prev = None
        
        if " " not in s:
            return len(s)

        for i in range(-1, -len(s)-1, -1):
            if s[i] != " ":
                counter += 1
                prev = s[i]
            else:
                if prev is not None:
                    if s[i] == ' ':
                        return counter

        return counter
                

s = Solution()
print(s.lengthOfLastWord("a "))