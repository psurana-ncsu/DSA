class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {i:-1 for i in nums1}
        stack = []
        for j in nums2:
            if len(stack)==0 or stack[-1]>j:
                stack.append(j)
            else:
                while len(stack)>0 and stack[-1]<j:
                    curr = stack.pop()
                    dic[curr]=j
                stack.append(j)
        for i in range(len(nums1)):
            nums1[i]=dic[nums1[i]]
        return nums1
        
