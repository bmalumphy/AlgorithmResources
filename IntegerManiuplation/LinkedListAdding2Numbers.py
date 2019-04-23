# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        while(l1 is not None and l2 is not None):
            newvalue = (carry + l1.val + l2.val) % 10
            if carry + l1.val + l2.val >= 10:
                carry = 1
            else:
                carry = 0
            current.next = ListNode(newvalue)
            current = current.next
            l1 = l1.next
            l2 = l2.next
           # print(current.val)
        while(l1 is not None):
            current.next = ListNode((carry + l1.val)%10)
            current = current.next
            if carry + l1.val >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
           # print(current.val)
        while(l2 is not None):
            current.next = ListNode((carry + l2.val)%10)
            current = current.next
            if carry +  l2.val >= 10:
                carry = 1
            else:
                carry = 0
            l2 = l2.next
            #print(current.val)
        if(carry > 0):
            current.next = ListNode(carry)
        return dummyHead.next