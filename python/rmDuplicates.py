from ListNode import (ListNode, ListMethods)
import unittest

class RemoveDuplicates:
	def rmDups(self, head):
		head
		prev=None
		curr=head
		delete=False
		while(curr!=None):
			if(delete):
				if(curr.next==None):
					if(prev==None):
						return None
					prev.next=None
					delete=False
				elif(curr.val!=curr.next.val):
					if(prev==None):
						head=curr.next
					else:
						prev.next=curr.next
					delete=False
			else:
				if(curr.next==None):
					pass
				elif(curr.val==curr.next.val):
					delete=True
				else:
					if(prev==None):
						prev=curr
					else:
						prev=prev.next
			curr=curr.next	
		return head

class TestRemoveDuplicates(unittest.TestCase):
	def testRmDups(self):
		ln=ListMethods()
		sol=RemoveDuplicates()
		self.failUnlessEqual(ln.listToArr(sol.rmDups(ln.makeList([1,2,2,3,4]))),[1,3,4])
		self.failUnlessEqual(ln.listToArr(sol.rmDups(ln.makeList([1,2,3,4]))),[1,2,3,4])
		self.failUnlessEqual(ln.listToArr(sol.rmDups(ln.makeList([2,2,3,4]))),[3,4])
		self.failUnlessEqual(ln.listToArr(sol.rmDups(ln.makeList([1,2,2,3,4,4]))),[1,3])
		self.failUnlessEqual(ln.listToArr(sol.rmDups(ln.makeList([1,2,2,2,3,4]))),[1,3,4])
		self.failUnlessEqual(ln.listToArr(sol.rmDups(ln.makeList([2,2,2]))),[])

if __name__=='__main__':
	unittest.main()	
