# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head):
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second string 
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 

        totalsum = 0
        first = head
        second = prev

        while second:
            totalsum = max(totalsum, first.val + second.val)
            first = first.next
            second = second.next

        print(totalsum)
        
            


def build_linked_list(arr):
    head = ListNode(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head

arr = [5,4,2,1]

head = build_linked_list(arr)

sol = Solution()
sol.pairSum(head)