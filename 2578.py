class Solution:
    def splitNum(self, num: int) -> int:
        arr = []
        while num:
            arr.append(num%10)
            num=num//10
        arr.sort()
        num1_arr = []
        num2_arr = []
        num1=0
        num2=0
        chance=True
        for i in range(len(arr)):
            if chance:
                num1=num1*10+arr[i]
                chance=False
            else:
                num2=num2*10+arr[i]
                chance=True
        return num1+num2      
