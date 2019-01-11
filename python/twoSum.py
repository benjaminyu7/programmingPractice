import unittest

class Solution:
	def binarySearch (self,numbers,toFind):
		if(len(numbers)==1):
			if(numbers[0]==toFind):
				return 0
			if(toFind<numbers[0]):
				return -1
			if(toFind>numbers[0]):
				return -2
		elif(len(numbers)==2):
			if (numbers[0]==toFind):
				return 0
			elif (numbers[1]==toFind):
				return 1
			else:
				if(toFind<numbers[0]):
					return -1
				if(toFind>numbers[1]):
					return -3
				else:
					return -2
		else:
			upper=len(numbers)-1
			index=upper//2
			if(toFind>numbers[index]):
				temp=self.binarySearch(numbers[index+1:],toFind)
				if(temp<0):
					return(temp-index-1)
				else:
					return (temp+index+1)
			elif(toFind<numbers[index]):
				temp=self.binarySearch(numbers[0:index],toFind)
				return temp 
			else:
 				return index
	def linearSearch (self,numbers,toFind):
		for x in range(0,len(numbers)):
			if (toFind==numbers[x]):
				return x
	def binaryInsert (self,numbers,insert):
		index=self.binarySearch(numbers,insert)
		if(index<0):
			index=-index-1
		if(index==len(numbers)):
			numbers.append(insert)
		else:
			numbers.insert(index,insert)
		return numbers


	def twoSum(self, nums,target):
		index1=0
		index2=0
		searched=[nums[0]]
		for x in range(1,len(nums)):
			index=self.binarySearch(searched,target-nums[x])
			if(index<0):
				self.binaryInsert(searched,nums[x])
			else:
				return [self.linearSearch(nums,target-nums[x]),x]

			
		
class TestBinarySearch(unittest.TestCase):
	def testTwoSum(self):
		sol=Solution()
		self.failUnlessEqual(sol.twoSum([1,2,3,4,5],5),[1,2])
		self.failUnlessEqual(sol.twoSum([1,2,2,4,5],4),[1,2])
		self.failUnlessEqual(sol.twoSum([1,2,2,4,5],6),[1,3])
		self.failUnlessEqual(sol.twoSum([5,4,3,4,1],6),[0,4])
		self.failUnlessEqual(sol.twoSum([5,4,3,2,1],3),[3,4])
		self.failUnlessEqual(sol.twoSum([5,4],9),[0,1])
	def testBinarySearch(self):
		sol=Solution()
		self.failUnlessEqual(sol.binarySearch([1,2,3],2),1)
		self.failUnlessEqual(sol.binarySearch([1,2,3,4,5],1),0)
		self.failUnlessEqual(sol.binarySearch([1,2,3,4,5],5),4)
		self.failUnlessEqual(sol.binarySearch([1,2,3,4,5,6],1),0)
		self.failUnlessEqual(sol.binarySearch([1,2,3,4,5,6],6),5)
		self.failUnlessEqual(sol.binarySearch([1,2],2),1)
		self.failUnlessEqual(sol.binarySearch([1,2],1),0)
		self.failUnlessEqual(sol.binarySearch([1],1),0)
		self.failUnlessEqual(sol.binarySearch([1,3],2),-2)
		self.failUnlessEqual(sol.binarySearch([1,3],0),-1)
		self.failUnlessEqual(sol.binarySearch([1,3],4),-3)
		self.failUnlessEqual(sol.binarySearch([2,3,4,5],1),-1)
		self.failUnlessEqual(sol.binarySearch([1,2,3,4],5),-5)
		self.failUnlessEqual(sol.binarySearch([2,3,4,5,6],1),-1)
		self.failUnlessEqual(sol.binarySearch([1,2,3,4,5],6),-6)
		self.failUnlessEqual(sol.binarySearch([1],2),-2)
		self.failUnlessEqual(sol.binarySearch([2],1),-1)
	def testLinearSearch(self):
		sol=Solution()
		self.failUnlessEqual(sol.linearSearch([1,2,3],1),0)
		self.failUnlessEqual(sol.linearSearch([1,2,3],3),2)
		self.failUnlessEqual(sol.linearSearch([1,2,3],2),1)
	def testBinaryInsert(self):
		sol=Solution()
		self.failUnlessEqual(sol.binaryInsert([1,3],2),[1,2,3])
		self.failUnlessEqual(sol.binaryInsert([2,3],1),[1,2,3])
		self.failUnlessEqual(sol.binaryInsert([1,2],3),[1,2,3])
		self.failUnlessEqual(sol.binaryInsert([1,2,3,5,6,7],4),[1,2,3,4,5,6,7])
		self.failUnlessEqual(sol.binaryInsert([2,3,4,5,6,7],1),[1,2,3,4,5,6,7])
		self.failUnlessEqual(sol.binaryInsert([1,2,3,4,5,6],7),[1,2,3,4,5,6,7])
		
	
if __name__=='__main__':
	unittest.main()
