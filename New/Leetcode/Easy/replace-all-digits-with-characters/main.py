def checkInt(c):
    try:
        int(c)
        return True
    except ValueError:
        return False

class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        result = ''
        prev = ''

        for i in s:
            checker = checkInt(i)
            if not checker:
                result += i
                prev = i
            else:
                result += chr(ord(prev) + int(i))

        return result
        
s = Solution()
print(s.replaceDigits("a1b2c3d4e"))