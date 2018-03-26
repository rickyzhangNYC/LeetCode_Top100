# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #Create head of linked list
        head = current = ListNode(0)
        #Create carry variable when digits summed are greater than 9
        carry = 0
        #Loop while either node has a digit or if last 2 nodes create a carry
        while(l1 != None or l2 != None or carry != 0):
            #Reset value for each digit
            value = 0
            #If node of first list isn't empty, add it to value and move pointer
            if l1 != None:
                value += l1.val
                l1 = l1.next
            if l2 != None:
            #If node of second list isn't empty, add it to value and move pointer
                value += l2.val
                l2 = l2.next
            #Add carry from previous digit summation to current value 
            value += carry
            #Calculate new carry from value
            carry = int(value/10)
            #Calculate single digit to be put into the resultant linked list
            value = value%10
            #Create node to put value into and move pointer to it 
            current.next = ListNode(value)
            current = current.next
        return head.next