# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def getMid(self , head , tail):
        mid = head
        fast = head
        while fast != head or fast.next is None:
            fast = fast.next.next
            mid = mid.next
        return mid
    
    def mergeTwoLists(self, list1 , list2):
        d=c=ListNode(0)
        
        while list1 and list2:
            if list1.val<list2.val:
                c.next=list1
                list1=list1.next
            else:
                c.next=list2
                list2=list2.next
            c=c.next
        c.next = list1 or list2
        return d.next
    
    def mergeSort(self , head , tail):
        if head == tail:
            n = ListNode(head.val)
            return n
        
        mid = self.getMid(head , tail)
        lhs = self.mergeSort(head , mid)
        uhs = self.mergeSort(mid.next , tail)
        
        ans = self.mergeTwoLists(lhs , uhs)
        return ans
        
        
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trav = head
        if trav is None:
            return None
        while trav.next is not None:
            trav = trav.next
        
        ans = self.mergeSort(head , trav)
        return ans
        
