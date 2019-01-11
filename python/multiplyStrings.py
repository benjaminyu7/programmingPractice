import unittest

class MultiplyStrings:
	def addStrings(self,str1,str2):
		index1=len(str1)-1
		index2=len(str2)-1
		strSum=''
		remainder=0

		while(index1>=0 or index2>=0):
			#add a single digit
			if(index1>=0 and index2>=0):
				temp=int(str1[index1])+int(str2[index2])+remainder
			elif(index1>=0):
				temp=int(str1[index1])+remainder
			else:
				temp=int(str2[index2])+remainder
			remainder=temp//10
			strSum= str(temp%10) +strSum

			index1-=1
			index2-=1
		if(remainder>0):
			strSum=str(remainder)+strSum
		return strSum
	def multiplyStrings(self,str1,str2):
		if(str1=="0" or str2=="0"):
			return '0'
		strProduct=''
		units=""
		for i in range(len(str2)-1,-1,-1):
			remainder=0
			tempSum=''
			for j in range(len(str1)-1,-1,-1):
				temp=int(str1[j])*int(str2[i])+remainder
				remainder=temp//10
				tempSum=str(temp%10)+tempSum
			if(remainder>0):
				tempSum=str(remainder)+tempSum
			strProduct=self.addStrings(strProduct,tempSum+units)
			units=units+'0'
		return strProduct


class TestStrings(unittest.TestCase):
	def testAddStrings(self):
		sol=MultiplyStrings()
		self.failUnlessEqual(sol.addStrings("123","456"),"579")
		self.failUnlessEqual(sol.addStrings("23","456"),"479")
		self.failUnlessEqual(sol.addStrings("125","250"),"375")
		self.failUnlessEqual(sol.addStrings("999","2"),"1001")
		self.failUnlessEqual(sol.addStrings("","456"),"456")
	def testMulStrings(self):
		sol=MultiplyStrings()
		self.failUnlessEqual(sol.multiplyStrings("12","11"), "132")
		self.failUnlessEqual(sol.multiplyStrings("2","11"), "22")
		self.failUnlessEqual(sol.multiplyStrings("121","11"), "1331")
		self.failUnlessEqual(sol.multiplyStrings("0","11"), "0")
		self.failUnlessEqual(sol.multiplyStrings("123","456"), "56088")
		self.failUnlessEqual(sol.multiplyStrings("15","15"), "225")
		self.failUnlessEqual(sol.multiplyStrings("25","25"), "625")
		self.failUnlessEqual(sol.multiplyStrings("25","15"), "375")

if (__name__=='__main__'):
	unittest.main()
