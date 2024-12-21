from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        nums.append(target)
        result = sorted(nums).index(target)
        return result
        
s = Solution()
print(s.searchInsert([1,3,5,6], 2))