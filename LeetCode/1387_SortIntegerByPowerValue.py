class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        #store all the intermediate result to save computations
        cache = {1:0}

        def recurse(num):
            if num ==1:
                return 0
            if num in cache.keys():
                return cache[num]
            if num%2==0:
                ans = 1+recurse(num//2)
                cache[num]=ans
            else:
                ans = 1+recurse(3*num+1)
                cache[num]=ans
            return cache[num]
            
        #store both power and num in a list
        pq = []
        for val in range(lo, hi+1):
            power = recurse(val)
            pq.append((power, val))

        pq.sort()
        return pq[k-1][1]
        
