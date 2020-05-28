import unittest
import addLargeNumbers
from Doublestack import DoubleStack

# 测试大数加法
# class addLargeNumbersTestCase(unittest.TestCase):
#
#     def test_addLargeNumbers(self):
#         sum_result = addLargeNumbers.operationAdd('123456789', '98765432111')
#         self.assertEqual(sum_result, '98888888900')


#　测试双头栈
class addLargeNumbersTestCase(unittest.TestCase):

    def test_DoubleStack(self):

        stack = DoubleStack(limit=10)
        self.assertEqual(stack.l_push(1), [1])
        self.assertEqual(stack.r_push(2), [1,2])
        self.assertEqual(stack.r_push(3), [1,2,3])
        self.assertEqual(stack.l_pop(), [2,3])
        self.assertEqual(stack.r_pop(), [2])
        self.assertEqual(stack.r_pop(), [])
        self.assertEqual(stack.r_pop(), [])

if __name__ == '__main__':
    unittest.main()