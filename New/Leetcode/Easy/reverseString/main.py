from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)):
            x = s.pop()
            s.insert(i, x)
        return s    
        
s = Solution()
print(s.reverseString(["h","e","l","l","o"])) #o l l e h