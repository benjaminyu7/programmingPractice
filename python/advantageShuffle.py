import unittest

class ValueIndex(object):
    def __init__(value, index):
        self.value = value
        self.index = index

class Solution:
	def solution(self, A, B):
		return 5

class TestAdvantageShuffle(unittest.TestCase):
	def testAddStrings(self):
		sol=Solution()
		self.failUnlessEqual(sol.addStrings("","456"),"456")
	def testMulStrings(self):
		sol=Solution()
		self.failUnlessEqual(sol.multiplyStrings("12","11"), "132")

if (__name__=='__main__'):
	unittest.main()
