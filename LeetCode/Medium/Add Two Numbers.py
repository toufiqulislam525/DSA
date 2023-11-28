# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x = l1
        y = l2
        mul1 = 1
        mul2 = 1
        num1 = 0
        num2 = 0

        while True:
            if x:
                num1+= x.val*mul1
                mul1*= 10
                x = x.next
            else:
                break
        while True:
            if y:
                num2+= y.val* mul2
                mul2*=10
                y = y.next
            else:
                break
                
            

        sum = num1+num2
        sum = str(sum)[::-1]
        
        
        output2 = ListNode(int(sum[0]))
        output = output2

        i = 0
        while i < len(sum) - 1:
            output.val = int(sum[i])
            output.next = ListNode(int(sum[i+1]))
            output = output.next
            i+=1
 
        return output2