import unittest

class Solution():
    def numMatchingSubseq(self, S, words):
        count = 0
        for sIndex in range (0, len(S)):
            for word in words:
                if(S[sIndex:sIndex+len(word)]==word):
                    #remove the word from words
                    count+=1
        return count

class TestSolution(unittest.TestCase):
    def testNumMatchingSubseq(self):
        sol = Solution()
        self.assertEqual(sol.numMatchingSubseq('abcd', ['abc','bcd', 'de']), 2)
        self.assertEqual(sol.numMatchingSubseq('abcd', ['abc','bcd', 'de', 'da']), 2)

if __name__=='__main__':
    unittest.main()


