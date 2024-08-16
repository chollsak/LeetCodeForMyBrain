class Solution:
    def thousandSeparator(self, n: int) -> str:
        string = str(n)
        newString = ''
        if len(string) < 4:
            return string
        else:
            count = 0
            for i in range(len(string) - 1, -1, -1):
                if count == 3:
                    newString += "."
                    newString += string[i]
                    count = 0
                else:
                    newString += string[i]
                count += 1
            return newString[::-1]
        
x = Solution
print(x.thousandSeparator(x, 987))
print(x.thousandSeparator(x, 1234342131))