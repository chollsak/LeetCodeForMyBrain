from typing import List

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    print("pivot", pivot)
    left = [x for x in arr if x[1] > pivot[1]]  # Sort in descending order by height
    middle = [x for x in arr if x[1] == pivot[1]]
    right = [x for x in arr if x[1] < pivot[1]]

    return quickSort(left) + middle + quickSort(right)

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = list(zip(names, heights))
        print("Zipped:", zipped)
        res = quickSort(zipped)
        return [i[0] for i in res]

# Example Usage
s = Solution()
print(s.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
