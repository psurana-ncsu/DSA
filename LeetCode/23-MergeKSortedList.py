# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(-1)
        curr = dummyhead
        while list1 or list2:
            if not list1:
                curr.next=list2
                curr=curr.next
                list2=list2.next
            elif not list2:
                curr.next=list1
                curr=curr.next
                list1=list1.next  
            elif list1.val>list2.val:
                curr.next=list2
                curr=curr.next
                list2=list2.next    
            else:
                curr.next=list1
                curr=curr.next
                list1=list1.next  
        return dummyhead.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==1:
            return lists[0]
        if len(lists)==0:
            return None
        l,r = 0, len(lists)-1
        mid = l+(r-l)//2
        l1 = self.mergeKLists(lists[0:mid+1])
        l2 = self.mergeKLists(lists[mid+1:r+1])
        return self.mergeTwoLists(l1,l2)
    
