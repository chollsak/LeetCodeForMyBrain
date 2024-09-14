def separate_digits(number):
    # Convert the number to a string and get each digit as an integer
    return [int(digit) for digit in str(number)]

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(number):
            # Compute the next number by summing the squares of its digits
            return sum(int(digit)**2 for digit in str(number))
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1

# Example usage
sol = Solution()
print(sol.isHappy(7))  # Output should be True

# Testing other numbers
print(sol.isHappy(19))  # Output should be True
print(sol.isHappy(2))   # Output should be False
print(sol.isHappy(1000))  # Example with thousands
print(sol.isHappy(2147483647))  # Example with upper bound
