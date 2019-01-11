import unittest

class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None

class ListMethods:
	def makeList(self, x):
		head = ListNode(x[0])
		tmp = head
		for i in range (1,len(x)):
			tmp.next=ListNode(x[i])
			tmp=tmp.next
		return head
	def printList(self, head):
		while(head!=None):
			print(head.val)
			head = head.next
	def listToArr(self, head):
		arr=[]
		while(head!=None):
			arr.append(head.val)
			head = head.next
		return arr

class TestNodes(unittest.TestCase):
	def testList(self):
		lm=ListMethods()
		self.failUnlessEqual(lm.listToArr(lm.makeList([1,2,3,4,5])),[1,2,3,4,5])

if __name__ == '__main__':
	unittest.main()
