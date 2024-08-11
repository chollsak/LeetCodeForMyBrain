from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = round(celsius + 273.15, 5)  #5 decimal
        fahrenheit = round(celsius * 1.80 + 32.00, 5)  #5 decimal
        return [kelvin, fahrenheit]
    

x = Solution()
print(x.convertTemperature(36.50)) 
