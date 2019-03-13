import unittest

class Solution(object):
    def simplifyEquation(self, equation):
        xValue = 0
        intValue = 0
        tempVal = '0'
        tempOperation='+'
        for char in equation:
            if (char == '-' or char=='+'):
                if(tempOperation == '-'):
                    intValue -= int(tempVal)
                else:
                    intValue += int(tempVal)
                tempVal='0'
                tempOperation = char
            elif (char == 'x'):
                if(tempVal=='0'):
                    tempVal = 1
                if(tempOperation == '-'):
                    xValue -= int(tempVal)
                elif(tempOperation == '+'):
                    xValue += int(tempVal)
                else:
                    xValue = int(tempVal)
                tempVal='0'
            else:
                if (tempVal=='0'):
                    tempVal=str(char)
                else:
                    tempVal+=str(char)
        if(tempOperation == '-'):
            intValue -= int(tempVal)
        elif(tempOperation == '+'):
            intValue += int(tempVal)
        return (xValue, intValue)
    def solveEquation(self, equation):
        sides = equation.split("=")
        (leftX, leftVal) = self.simplifyEquation(sides[0])
        (rightX, rightVal) = self.simplifyEquation(sides[1])
        xVal = leftX - rightX
        intVal = rightVal - leftVal
        if(xVal==0 and intVal==0):
            return "Infinite solutions"
        elif(xVal==0 and intVal!=0):
            return "No solution"
        else:
            return "x="+str(intVal/xVal)

class TestStringMethods(unittest.TestCase):
    def testSimplifyEquation(self):
        sol = Solution()
        self.assertEqual(sol.simplifyEquation('2x+3x+6x'),(11,0))
        self.assertEqual(sol.simplifyEquation('-2x+3x+6x'),(7,0))
        self.assertEqual(sol.simplifyEquation('-4x+3x'),(-1,0))
        self.assertEqual(sol.simplifyEquation('2+3+6'),(0,11))
        self.assertEqual(sol.simplifyEquation("x+5-3+x"),(2,2))
        self.assertEqual(sol.simplifyEquation('6+x-2'),(1,4))
        self.assertEqual(sol.simplifyEquation('-x'),(-1,0))
        self.assertEqual(sol.simplifyEquation('1'),(0,1))
    def testSolveEquation(self):
        sol = Solution()
        self.assertEqual(sol.solveEquation('2x+1=x+7'),'x=6')
        self.assertEqual(sol.solveEquation("x+5-3+x=6+x-2"),'x=2')
        self.assertEqual(sol.solveEquation('2x+=x+'),'x=0')
        self.assertEqual(sol.solveEquation('-x=1'),'x=-1')
        self.assertEqual(sol.solveEquation('2x+1=2x+7'),'No solution')
        self.assertEqual(sol.solveEquation('2x+7=2x+7'),'Infinite solutions')

if __name__ == '__main__':
    unittest.main()
