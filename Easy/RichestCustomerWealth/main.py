from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for index in accounts:
            temp = sum(index)
            if temp >= max:
                max = temp
        
        return(max)

x = Solution
x.maximumWealth(x, [[1,2,3],[3,2,1]])
x.maximumWealth(x, [[2,8,7],[7,1,3],[1,9,5]])
