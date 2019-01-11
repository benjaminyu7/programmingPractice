import unittest
class Solution(object):
	def nthUglyNumber(self, n):
		ugNum=[1,2,3,4,5]
		if(n<=5):
			return ugNum[n-1]
		x=5
		index2 = index3 = index5 = 0
		while (x<n): 
			min = 2*ugNum[index2]
			minDex = 2
			if(3*ugNum[index3]< min):
				min = 3*ugNum[index3]
				minDex = 3
			if(5*ugNum[index5]< min):
				min = 5*ugNum[index5]
				minDex = 5
			if(min > ugNum[x-1]):
				ugNum.append(min)
				x=x+1
			if(minDex==2):
				index2=index2+1
			elif(minDex==3):
				index3=index3+1
			elif(minDex==5):
				index5=index5+1
		print(ugNum)
		return ugNum[n-1]
	
class TestUgly(unittest.TestCase):
	def testUgNum(self):
		sol=Solution()
		self.failUnlessEqual(sol.nthUglyNumber(1),1)
		self.failUnlessEqual(sol.nthUglyNumber(5),5)
		self.failUnlessEqual(sol.nthUglyNumber(10),12)
		self.failUnlessEqual(sol.nthUglyNumber(20),36)

if __name__=='__main__':
	sol = Solution()
	sol.nthUglyNumber(1690)
