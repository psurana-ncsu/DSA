class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        curr = ""
        s=0
        d=0
        m, n = len(name), len(typed)
        while s<m and d<n:
            if name[s]==typed[d]:
                curr = name[s]
                s+=1
                d+=1
            elif curr=="":
                return False
            else:
                while d<n and typed[d]==curr:
                    d+=1
                curr= ""
        while d<n and typed[d]==curr:
            d+=1
        return True if s==m and d==n else False
        
