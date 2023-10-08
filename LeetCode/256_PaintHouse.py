class Solution:  
    def minCost(self, costs: List[List[int]]) -> int:
        #Bottom up approach
        n = len(costs)
        #Otimise space by using three variables to store the previous results instead of creating an entire matrix
        #consider first second and third are the 3 colors
        first, second, third=0,0,0
        for i in range(n):
            #At any point, previous and curr color wont be the same i.e. choose from other two color
            costs[i][0]+=min(second, third)
            costs[i][1]+=min(first, third)
            costs[i][2]+=min(first, second)
            third = costs[i][2]
            first = costs[i][0]
            second = costs[i][1]
        return min(costs[n-1])
        
