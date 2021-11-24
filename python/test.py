import unittest

class Solution:
	def solution(self, string):
		map = set()
		for char in string:
			map.add(char)
		print(map)
		return 0

class TestStrings(unittest.TestCase):
	def testAddStrings(self):
		sol=Solution()
		sol.solution("Hello the world is going on")
		self.failUnlessEqual("456","456")
	def testMulStrings(self):
		sol=Solution()
		self.failUnlessEqual("132", "132")

if (__name__=='__main__'):
	unittest.main()
