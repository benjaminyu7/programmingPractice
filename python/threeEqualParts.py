class Solution(object):
    def binaryToDecimal(self, arr):
        value=0
        for x in arr:
            value=value*2
            value=value+x
        return value
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        count = 0
        #count the number of ones
        for x in A:
            if(x == 1):
                count=count+1
        if(count%3!=0):
            return [-1,-1]
        if(count==0):
            return[0,len(A)-1]
        
        #make the partitions
        numOnes=count/3
        count = 0
        answer1=-1
        answer2=-1
        for x in range (len(A)-1,-1,-1):
            if(A[x]==1):
                count=count+1
            if(count==numOnes):
                if(answer2==-1):
                    answer2=x+1
                elif(answer1==-1):
                    answer1=x
                count = 0
        part1 = self.binaryToDecimal(A[:answer1+1])
        part2 = self.binaryToDecimal(A[answer1+1:answer2])
        part3 = self.binaryToDecimal(A[answer2:])
        if (part1==part2 and part2==part3):
            return [answer1,answer2]
        return [-1,-1]
sol = Solution()
print(sol.threeEqualParts([1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0]))
