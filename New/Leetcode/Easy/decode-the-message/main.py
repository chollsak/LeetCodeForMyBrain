class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        index = []
        temp = []
        couter = 97
        result = ''
        for i in key:
            if i not in temp:
                if i != " ":
                    temp.append(i)
                    index.append(couter)
                    couter+=1 

        for j in message:
            if j != " ":
                idx = temp.index(j)
                result += chr(index[idx])
            else:
                result += " "

        return result
            

        
s = Solution()
print(s.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))