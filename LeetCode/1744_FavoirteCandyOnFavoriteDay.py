class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for val in candiesCount:
            prefix.append(prefix[-1]+val)
        ans = []
        for ftype, day, cap in queries:
            left = prefix[ftype+1]//(day+1)
            if left>0 and prefix[ftype]<cap*(day+1):
                ans.append(True)
            else:
                ans.append(False)
        return ans

        
