class Solution:
    def scoreOfString(self, s: str) -> int:
        stack = []
        prev = 0
        for char in s:
            ascii_value = ord(char)
            stack.append(abs(ascii_value-prev))
            prev = ascii_value
        
        stack.pop(0)
        return sum(stack)
       
            
        

x = Solution
print(x.scoreOfString(x, "zaz"))