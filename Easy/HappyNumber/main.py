def separate_digits(number):
    number_str = str(number)
    
    digits = []
    
    for digit in number_str:

        digits.append(int(digit))
    
    return digits

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(number):
            """
            :type number: int
            :rtype: int
            """
            number_str = str(number)
            
            sum_of_squares = 0
            
            for digit in number_str:

                sum_of_squares += int(digit) ** 2
            
            return sum_of_squares
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)

            n = get_next(n)
        
        return n == 1

sol = Solution()
print(sol.isHappy(7)) 

print(sol.isHappy(19)) 
print(sol.isHappy(2))   
print(sol.isHappy(1000))  
print(sol.isHappy(2147483647))  
