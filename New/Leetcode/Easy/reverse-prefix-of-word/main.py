class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = ''
        for i in word:
            if i == ch:
                index = word.index(i)
                for j in range(index, -1, -1):
                    result += word[j]

                for r in range(index+1, len(word)):
                    result += word[r]
                
                return result
        return word


        
s = Solution()
print(s.reversePrefix("xyxzxe", "z"))