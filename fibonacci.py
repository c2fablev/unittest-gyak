import unittest

def fibo(n :int):
    tmp = 1
    prevTmp = 0
    prevTmp2 = 0
    if n <= 0:
        return 0
    for i in range(0,int(n)-1):
        prevTmp2 = prevTmp
        prevTmp = tmp
        tmp = prevTmp + prevTmp2
    return tmp

class TestFibonacci(unittest.TestCase):
    def test_Negative(self):
        self.assertEqual(fibo(-2), 0)
    def test_isWorking(self):
        self.assertEqual(fibo(10), 55)
    def test_floatNum(self):
        self.assertGreater(fibo(2.3), 0)
    def test_equalOrGrater(self):
        self.assertGreaterEqual(fibo(5), 5)
    def test_equalOrLess(self):
        self.assertLessEqual(fibo(3), 2)

if __name__ == '__main__':
  unittest.main()
  