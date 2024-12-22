from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempArr = []
        result = []

        for index, val in enumerate(nums):
            complement = target - val # val1 + val2 = target -> val2 = target - val1
            
            if complement in tempArr: 
                firstIndex = tempArr.index(complement)
                result.append(firstIndex)
                result.append(index) 
                return result
        
            tempArr.append(val) 

        return result
  
s = Solution()
print(s.twoSum([3,2,4],6))

