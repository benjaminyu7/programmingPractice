import unittest

class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None

class Solution(object):
        def arrToList(self,arr):
                head=ListNode(arr[0])
                current=head
                for x in range(1,len(arr)-1):
                        current.next=arr[x]
                        current=current.next
                return head
        def numToArr(self,num):
                head=ListNode(num%10)
                if(num>=10):
                    current=head
                    num=num//10
                    while(num>=10):
                            current.next=ListNode(num%10)
                            num=num//10
                            current=current.next
                    current.next=ListNode(num)
                return head
                
        def reverseList(self,head):
                newHead=head
                head = head.next
                current = head
                newHead.next = None
                while(head!=None):
                        current = head
                        head=head.next
                        current.next=newHead
                        newHead=current
                return newHead
        def addTwoNumbers(self,l1,l2):
                unit=1
                num=0
                
                while(l1!=None and l2!=None):
                        num = num + (l1.val+l2.val)*unit
                        l1 = l1.next
                        l2 = l2.next
                        unit = unit*10
                while(l1!=None):
                        num = num + (l1.val)*unit
                        l1 = l1.next
                        unit = unit*10
                while(l2!=None):
                        num = num + (l2.val)*unit
                        l2 = l2.next
                        unit = unit*10
                print(num)
                return self.numToArr(num)
class testSolution(unittest.TestCase):
	def testArrList(self):
		sol=Solution()
	
sol=Solution()
temp=sol.arrToList([1,2,3])
temp=sol.reverseList(temp)
while(temp!=None):
	print(temp.val,", ")
	temp=temp.next
