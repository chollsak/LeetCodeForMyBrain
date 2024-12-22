from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s) #check key here

        for val in anagram_map.values():
            result.append(val)

        result.sort(key=lambda x: len(x))
        return result

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))