class Solution:
    def isBalanced(self, num: str) -> bool:
        oddN = 0
        evenN = 0

        for i in range(len(num)):
            if i % 2 == 0:
                evenN += int(num[i])
            else:
                oddN += int(num[i])

        return oddN == evenN
        
        
s = Solution()
print(s.isBalanced("1234"))