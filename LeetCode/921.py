class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        moves = 0
        for ch in s:
            if ch=="(":
                left+=1
            elif ch==")" and left>0:
                left-=1
            else:
                moves+=1
        return left+moves
        
