class Solution(object):
    def kInversePairsHelper(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if(n<2 and k>0):
            return -1
        elif(n==2 and k==1):
            return 0
        elif(k==0):
            return 0
        temp1=self.kInversePairsHelper(n-1,k)
        temp2=self.kInversePairsHelper(n-1,k-1)
        if(temp1 == -1 and temp2==-1):
            return -1
        if(temp1 == -1):
            temp1=0
	else:
	    temp1+=1
        if(temp2 == -1):
            temp2=0
        else:
            temp2+=1
        return temp1+temp2
    def kInversePairs(self,n,k):
        if(n<2 and k>0):
            return 0
        elif(n==2 and k==1):
            return 1
        elif(k==0):
            return 1
        else:
            return self.kInversePairsHelper(n,k)
sol = Solution()
print(sol.kInversePairs(5,2))
