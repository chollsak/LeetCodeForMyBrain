from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ls = []
        for i in arr:

            if i % 2 == 1:
                ls.append(i)
                if len(ls) >= 3:
                    return True
            else:
                ls.clear()
            
        return False
            

x = Solution
print(x.threeConsecutiveOdds(x, [1,2,34,3,4,5,7,23,12]))
print(x.threeConsecutiveOdds(x, [2,6,4,1]))