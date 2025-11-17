import unittest

def fibo(n :int):
    tmp = 1
    prevTmp = 0
    prevTmp2 = 0
    if n <= 0:
        return 0
    for i in range(0,n-1):
        prevTmp2 = prevTmp
        prevTmp = tmp
        tmp = prevTmp + prevTmp2
    return tmp

class TestFibonacci(unittest.TestCase):
    def Negative(self):
        self.assertEqual(fibo(-2), 0)
    def isWorking(self):
        self.assertEqual(fibo(10), 55)
    def floatNum(self):
        self.assertGreater(fibo(2.3), 0)
    def equalOrGrater(self):
        self.assertGreaterEqual(fibo(5), 5)
    def equalOrLess(self):
        self.assertLessEqual(fibo(3), 2)