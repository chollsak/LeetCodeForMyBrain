class Solution:
    def getSum(arr):
        summ = 0
        for j in range(len(arr)):
            summ += arr[j]
        print(summ)
        return summ
    
    def getTempArr(n):
        digits = list(str(n))
        temp = []

        for i in digits:
            temp.append(int(i)*int(i))
        
        print(temp)
        return temp

    def isHappy(self, n: int) -> bool:
        temp = Solution.getTempArr(n)
        summ = Solution.getSum(temp)
        while True:
            if summ < 10:
                if summ != 1 and summ != 7: 
                    return False
                else:
                    return True
            else:
                temp = Solution.getTempArr(summ)
                summ = Solution.getSum(temp)
                print(summ)
                

s = Solution()
print(s.isHappy(1111111))