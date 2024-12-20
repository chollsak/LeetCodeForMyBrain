class Solution:
    def isValid(self, s: str) -> bool:
        char = list(s)

        if(len(char) % 2 != 0):
            return False
        else:
            i = 0
            while i < len(char):
                if len(char) == 0:
                    return True
                else:
                    if i+1 < len(char):
                        if char[i] == '{' and char[i+1] == '}' or char[i] == '(' and char[i+1] == ')' or char[i] == '[' and char[i+1] == ']': 
                            print(char)
                            char.pop(i+1)
                            char.pop(i)
                            i = 0
                        else:
                            i += 1
                    else:
                        i += 1
        
        return len(char) == 0
                        
s = Solution()
print(s.isValid("([])"))