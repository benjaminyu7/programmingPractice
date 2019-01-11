class Solution(object):
    def getNthdigit(self, num, digit):
        digitNum = 0
        temp = num
        while(num>10):
            num=num//10
            digitNum=digitNum+1
        if(num==10):
            digitNum=digitNum+2
        else:
            digitNum=digitNum+1
        if(digit>digitNum):
	    print(num)
	    print(digit)
	    print(digitNum)
            return -1
        else:
            for x in range(0, digitNum-digit):
                temp=temp//10
            return temp%10
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
	n=n-1
        currentDigit=9
        sequenceDigit=1
        tempNum=0
        magnitude=10
        digits=1
        while (currentDigit<=n):
            #update the current digit range
            magnitude=magnitude*10
            digits=digits+1
            currentDigit=currentDigit+(magnitude-magnitude/10)*digits
        #utilize the magnitude and currentDigit to find the number
        currentDigit=currentDigit-(magnitude-magnitude/10)*digits
        #base/lower bound
        magnitude = magnitude/10-1
        #find number
        n=n-currentDigit
        tempNum=magnitude+n//digits+1
        tempIndex=n%digits + 1
        #return digit
        return self.getNthdigit(tempNum, tempIndex)
sol = Solution()
for x in range (100,1000):
	print(x),
	print(": "),
	print(sol.findNthDigit(x))
