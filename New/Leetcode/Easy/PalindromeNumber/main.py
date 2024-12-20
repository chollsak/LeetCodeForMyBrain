class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits= list(str(x))
        for i in range(len(digits)):
            if digits[i] != digits[-i-1]:
                return False
        return True
        

s = Solution()
print(s.isPalindrome(-121))