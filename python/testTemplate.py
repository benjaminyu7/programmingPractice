import unittest

class Solution:
	def solution(self):
		return 5

class TestStrings(unittest.TestCase):
	def testAddStrings(self):
		sol=Solution()
		self.failUnlessEqual(sol.addStrings("","456"),"456")
	def testMulStrings(self):
		sol=Solution()
		self.failUnlessEqual(sol.multiplyStrings("12","11"), "132")

if (__name__=='__main__'):
	unittest.main()
