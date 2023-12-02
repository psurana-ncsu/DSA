///
Q1) You are given a sorted array of integers A and an int k. You can take some portion of k and add it to any integer in A. 
You can repeat this process until k is exhausted. 
The final aim is to maximize the number of integer that are same in the array. How would you do it?

Ex 1: A = [1,4,5,10,11,12] and k=4.
Step 1: Take 2 from k and add it to 10. Now, A = [1,4,5,12,11,12], k=2
Step 2: Take 1 from k and add it to 11. Now, A = [1,4,5,12,12,12], k=1
Now we cannot do anything as no other element can be made equal to 12. Thus we stop here.
///

def solution(arr, k):
    n = len(arr)
    ans = 0
    total = 0
    left = 0
    
    for right in range(n):
        total += arr[right]
        
        while arr[right] * (right - left + 1) - total > k:
            total -= arr[left]
            left += 1

        ans = max(ans, right - left + 1)

    return ans
v, t = [1,4,5,10,11,12], 4
result = solution(v, t)
print(result)
print("Hello world")
