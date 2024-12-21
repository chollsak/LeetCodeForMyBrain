class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        result = ""

        for i in range(len(arr)):
            print(arr[i])
            for j in range(len(arr[i])-1, -1, -1):
                result += arr[i][j]
            if i+1 < len(arr):
                result += " "
        
        return result
        
s = Solution()
print(s.reverseWords("Mr Ding"))