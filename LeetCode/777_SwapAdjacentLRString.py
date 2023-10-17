class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        r=0
        l=0
        n = len(start)
        for i in range(n):
            if start[i]=="L" and end[i]=="R" or start[i]=="R" and end[i]=="L":
                return False
            if r>0 and start[i]=="L":
                return False
            if start[i]==end[i] and r==0 and l==0:
                continue
            if start[i]=="R" and l>0:
                return False
            if start[i]=="R" and end[i]=="X":
                r+=1
                continue
            if r>0 and start[i]=="X" and end[i]=="R":
                r-=1
                continue
            if start[i]=="X" and end[i]=="L":
                l+=1
                continue
            if l>0 and start[i]=="L" and end[i]=="X":
                l-=1
                continue
            elif l<=0 and start[i]=="L" and end[i]=="X":
                return False
        if r!=0 or l!=0:
            return False
        return True
            
        
