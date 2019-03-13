import unittest

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempCount = 0
        maxCount = 0
        for num in nums:
            if (num==0):
                maxCount = max(tempCount, maxCount)
                tempCount = 0
            else: 
                tempCount += 1
        maxCount = max(tempCount, maxCount)
        return maxCount 

class TestSolution(unittest.TestCase):
    def testMaxConsecutiveOnes(self):
        sol = Solution()
        self.assertEqual(sol.findMaxConsecutiveOnes([1,1,1,0,1,1]),3)
        self.assertEqual(sol.findMaxConsecutiveOnes([0,1,1,1,0,1,1]),3)
        self.assertEqual(sol.findMaxConsecutiveOnes([0,1,1,1,0,1,1,0]),3)
        self.assertEqual(sol.findMaxConsecutiveOnes([1,1,1,0,1,1,0]),3)
        self.assertEqual(sol.findMaxConsecutiveOnes([]),0)
        self.assertEqual(sol.findMaxConsecutiveOnes([0]),0)
        self.assertEqual(sol.findMaxConsecutiveOnes([1]),1)
        self.assertEqual(sol.findMaxConsecutiveOnes([1,1,1,1,1,1]),6)

if __name__ =='__main__':
    unittest.main()
