from typing import List
from itertools import combinations

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def find_and_remove_repeated_list(arrays):
            seen = set()  # To store unique lists
            unique_arrays = []
            for array in arrays:
                t_array = tuple(sorted(array))  # Convert list to tuple for set storage
                if t_array not in seen:
                    seen.add(t_array)
                    unique_arrays.append(array)
            return unique_arrays
        
        candidates.sort()  # Sort candidates to handle duplicates
        storage = []
        n = len(candidates)
        
        # Generate all possible combinations
        for r in range(1, n + 1):
            for combo in combinations(candidates, r):
                if sum(combo) == target:
                    storage.append(list(combo))
        
        # Remove any duplicates from the final result
        storage = find_and_remove_repeated_list(storage)
        return storage

# Test the function
x = Solution()
print(x.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
