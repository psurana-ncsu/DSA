class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        curr = "a"
        base=96
        for c in word:
            if curr!=c:
                temp = (ord("z")-ord(curr)+ord(c)-96)%26
                move = min(temp, 26-temp)
                ans+=move
                curr=c
            ans+=1
        return ans
        
