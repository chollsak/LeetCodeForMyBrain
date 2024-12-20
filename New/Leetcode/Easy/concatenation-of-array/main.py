from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = nums
        print(arr)

        for i in range(len(arr)):
            arr.append(nums[i])
        return(arr)

s = Solution()
print(s.getConcatenation([1,2,1]))