class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = num
        counter = 0
        while result != 0:
            if result % 2 == 0:
                result = result / 2
            else:
                result = result - 1
            counter += 1
        return counter
        
s = Solution()
print(s.numberOfSteps(123))