import unittest

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for char in s:
            if(char==']'):
                peek = stack.pop()
                tempString = ''
                repeats = ''
                concatedString = ''
                while(peek != '['):
                    tempString = peek+tempString
                    peek = stack.pop()
                while (len(stack)>0 and stack[-1].isdigit()):
                    peek = stack.pop()
                    repeats = peek+repeats
                for repeat in range (0,int(repeats)):
                    concatedString+=tempString        
                stack.append(concatedString)
            else:
                stack.append(char)
        decodedString=''
        while (len(stack)>0):
            decodedString=stack.pop()+decodedString
        return decodedString

class TestDecodeString(unittest.TestCase):
    def testAddStrings(self):
        sol=Solution()
        self.failUnlessEqual(sol.decodeString("3[a]2[b]"),"aaabb")
        self.failUnlessEqual(sol.decodeString("3[2[a]1[cd]]2[b]"),"aacdaacdaacdbb")
        self.failUnlessEqual(sol.decodeString(""),"")
        self.failUnlessEqual(sol.decodeString("abcd"),"abcd")

if (__name__=='__main__'):
    unittest.main()
