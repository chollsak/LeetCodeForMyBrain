from typing import List
from decimal import Decimal

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelv = celsius + 273.15
        fahr = celsius * 1.80 + 32.00

        return [
            float(Decimal(kelv).quantize(Decimal('0.00000'))),
            float(Decimal(fahr).quantize(Decimal('0.00000')))
        ]
        
s = Solution()
print(s.convertTemperature(36.50))