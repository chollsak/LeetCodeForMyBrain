from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int(''.join(map(str, digits)))
        result = []

        for i in range(len(str(n+1))):
            result.append(int(str(n+1)[i]))

        return result


s = Solution()
print(s.plusOne([4,3,2,1]))