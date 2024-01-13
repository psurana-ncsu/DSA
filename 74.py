class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        row=0
        while top<=bottom:
            mid = top+(bottom-top)//2
            if matrix[mid][0]>target:
                bottom=mid-1
            elif matrix[mid][n-1]<target:
                top=mid+1
            else:
                row=mid
                break
        l, r = 0, n-1
        while l<=r:
            mid = l+(r-l)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                l=mid+1
            else:
                r=mid-1

        return False
