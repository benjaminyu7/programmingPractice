import unittest

class Solution():

    def __init__(self):
        self.heap = []

    def insert(self, num):
        self.heap.append(num)
        self.heapify(len(self.heap) - 1)
        print(self.heap)

    def heapify(self, position):
        pointer = position
        while pointer > 0 and self.heap[pointer] < self.heap[(pointer-1)//2]:
            self.swap(pointer, pointer//2)
            pointer = pointer//2
        return True

    def heapify_down(self):
        pointer = 0
        while(self.get_left_child(pointer) < len(self.heap)):
            right = self.get_right_child(pointer)
            if(self.heap[self.get_left_child(pointer)] < self.heap[pointer]):
                self.swap(self.get_left_child(pointer), pointer)
                pointer = self.get_left_child(pointer)
            elif(right < len(self.heap) and self.heap[right] < self.heap[pointer]):
                self.swap(right, pointer)
                pointer = right
            else:
                break

    def swap(self, position_one, position_two):
        temp = self.heap[position_one]
        self.heap[position_one] = self.heap[position_two]
        self.heap[position_two] = temp

    def get_left_child(self, position):
        return 2 * position + 1

    def get_right_child(self, position):
        return 2 * position + 2

    def pop(self):
        # Todo: swap the root with the end leaf node
        ans = self.heap.pop(0)
        # Call heapify down in case the first heapify shifts a non_min value to the root
        self.heapify_down()
        self.heapify_down()
        return ans
    
    

class TestStrings(unittest.TestCase):
    def test_insert(self):
        sol=Solution()
        sol.insert(4)
        sol.insert(2)
        sol.insert(3)
        sol.insert(1)
        self.assertEqual(sol.pop(),1)
        self.assertEqual(sol.pop(),2)
        self.assertEqual(sol.pop(),3)
        self.assertEqual(sol.pop(),4)
    
    def test_double_heapify(self):
        sol=Solution()
        sol.insert(2)
        sol.insert(4)
        sol.insert(3)
        sol.insert(1)

        self.assertEqual(sol.pop(),1)
        self.assertEqual(sol.pop(),2)
        self.assertEqual(sol.pop(),3)
        self.assertEqual(sol.pop(),4)

if (__name__=='__main__'):
    unittest.main()

