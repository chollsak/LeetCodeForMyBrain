from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        newString = [''] * len(s)

        for i, index in enumerate(indices):
            newString[index] = s[i]
        
        return ''.join(newString)

x = Solution()
print(x.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])) 