# coding=utf-8
import unittest
import numpy as np


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        """Test method np.add(a, b)"""
        self.assertEqual(3, np.add(1, 2))
        self.assertNotEqual(3, np.add(2, 2))

    def test_minus(self):
        """Test method np.subtract(a, b)"""
        self.assertEqual(1, np.subtract(3, 2))

    def test_multi(self):
        """Test method np.multiply(a, b)"""
        self.assertEqual(6, np.multiply(2, 3))

    def test_divide(self):
        """Test method np.divide(a, b)"""
        self.assertEqual(2, np.divide(6, 3))
        self.assertEqual(2.5, np.divide(5, 2))


if __name__ == '__main__':
    """
    verbosity 可取值为 0, 1, 2:
        0 (静默模式): 只能获得总的测试用例数和总的结果, 比如总共100个: 失败20 成功80；
        1 (默认模式): 类似静默模式, 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”;
        2 (详细模式): 测试结果会显示每个测试用例的所有相关的信息.
    """
    unittest.main(verbosity=2)
