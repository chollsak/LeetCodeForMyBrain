class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jl = list(jewels)
        count = 0
        for index in stones:
            if index in jl:
                count += 1
        return count    
        

x = Solution
print(x.numJewelsInStones(x, "aA", "aAAbbbb"))
print(x.numJewelsInStones(x, "z", "ZZ"))