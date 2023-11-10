import math

import unittest

def add_frac(frac1, frac2):
    denominator=frac1[1]*frac2[1]
    numerator=frac1[0]*frac2[1]+frac1[1]*frac2[0]
    result=frac_fix(numerator,denominator)
    return result

def sub_frac(frac1, frac2): 
    denominator=frac1[1]*frac2[1]
    numerator=frac1[0]*frac2[1]-frac2[0]*frac1[1]
    result=frac_fix(numerator,denominator)
    return result

def mul_frac(frac1, frac2): 
    denominator=frac1[1]*frac2[1]
    numerator=frac1[0]*frac2[0]
    result=frac_fix(numerator,denominator)
    return result
    
def div_frac(frac1, frac2): 
    inverse=[frac2[1],frac2[0]]
    result=mul_frac(frac1,inverse)
    return result
    

def is_positive(frac): 
    return (frac[0]>0 and frac[1]>0) or (frac[0]<0 and frac[1]<0)

def is_zero(frac): 
    return frac[0]==0

def cmp_frac(frac1, frac2): 
    diff = sub_frac(frac1, frac2)
    if diff[0] > 0:
        return 1
    elif diff[0] < 0:
        return -1
    else:
        return 0
    
def frac2float(frac): 
    return frac[0] / frac[1]    

def frac_fix(numerator,denominator):
    number=math.gcd(numerator, denominator)
    result=[numerator//number,denominator//number]
    return result
    
    

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)



class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 5], [3, 5]), [1, 1])
        self.assertEqual(add_frac([1, 4], [1, 4]), [1, 2])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([5, 8], [3, 8]), [1, 4])
        self.assertEqual(sub_frac([5, 8], [1, 8]), [1, 2])
        self.assertEqual(sub_frac([3, 7], [2, 7]), [1, 7])


    def test_mul_frac(self): 
        self.assertEqual(mul_frac([3, 4], [2, 3]), [1, 2])
        self.assertEqual(mul_frac([2, 5], [3, 4]), [3, 10])
        self.assertEqual(mul_frac([1, 2], [1, 2]), [1, 4])

    def test_div_frac(self): 
        self.assertEqual(div_frac([3, 5], [4, 3]), [9, 20])
        self.assertEqual(div_frac([1, 2], [3, 4]), [2, 3])
        self.assertEqual(div_frac([3, 8], [1, 3]), [9, 8])

    def test_is_positive(self): 
        self.assertTrue(is_positive([4, 5]))
        self.assertFalse(is_positive([-3, 7]))
        

    def test_is_zero(self): 
        self.assertTrue(is_zero([0, 6]))
        self.assertFalse(is_zero([4, 5]))
        self.assertTrue(is_zero([0, 100]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([3, 5], [2, 5]), 1)
        self.assertEqual(cmp_frac([3, 5], [3, 5]), 0)
        self.assertEqual(cmp_frac([3, 5], [4, 5]), -1)
        self.assertEqual(cmp_frac([1, 7], [2, 14]), 0)
        self.assertEqual(cmp_frac([1, 8], [2, 16]), 0) 
        
    def test_frac2float(self): 
        self.assertEqual(frac2float([3, 4]), 0.75)
        self.assertEqual(frac2float([1, 3]), 1/3)
        self.assertEqual(frac2float([1, 2]), 0.5)


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy