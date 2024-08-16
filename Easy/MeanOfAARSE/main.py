from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        percentage = 5
        n = len(arr)
        timeOfRemove = int((percentage / 100) * n)

        for _ in range(timeOfRemove):
            if arr:
                arr.remove(min(arr))
                arr.remove(max(arr))
        result = round(sum(arr)/len(arr),  5)
        return result
        
x = Solution
print(x.trimMean(x,[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))
x.trimMean(x,[6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4])
x.trimMean(x,[6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0])