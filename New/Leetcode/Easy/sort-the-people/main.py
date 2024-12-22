from typing import List

def bubbleSort(arr):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1):
            if arr[i][1] < arr[i+1][1]:
                swap(i, i+1, arr)
                isSorted = False
    return arr
    
def swap(i, j , arr):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = list(zip(names, heights))
        print(zipped)
        res = bubbleSort(zipped)
        return [i[0] for i in res]
        
s = Solution()
print(s.sortPeople(["Mary","John","Emma"], [180,165,170]))