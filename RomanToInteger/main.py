class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0

        for char in s:
            value = roman[char]
            if value > prev_value:
                total += (value - (2 * prev_value)) #main algorithms to check lower char that is before the higher char
            else: 
                total += value
            prev_value = value

        return total


x = Solution()

print(x.romanToInt("III"))  
print(x.romanToInt("LVIII")) 
print(x.romanToInt("MCMXCIV"))  


'''Explanation
- Roman Numerals Dictionary: roman is a dictionary that maps Roman numeral characters to their corresponding integer values.

- Total Calculation:
        -If the current numeral’s value (value) is greater than the previous numeral’s value (prev_value), it means a subtraction scenario (like "IV" where V > I).
        -In this case, you subtract twice the previous value (total += value - 2 * prev_value) because it was added once in the previous iteration.
        -Otherwise, you simply add the current value.

- Updating prev_value: This is updated to the current numeral's value for use in the next iteration.'''