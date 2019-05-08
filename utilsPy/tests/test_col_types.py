import unittest
import pandas as pd

from utilsPy.col_types import col_types as ct

class col_types_TestClass(unittest.TestCase):
 
    def __init__(self, *args, **kwargs):

        super(col_types_TestClass, self).__init__(*args, **kwargs)

        self.dct = {'A': [1,2,3],
                    'B': [1.0, 2.0, 3.0],
                    'C': [1j, 2j, 3j],
                    'D': ['a', 'b', 'd'],
                    'E': [True, False, True]}

        self.df = pd.DataFrame(self.dct)

    def test_test_ser_str(self):
        self.assertFalse(ct.test_ser_str(self.df['A']))
        self.assertFalse(ct.test_ser_str(self.df['B']))
        self.assertFalse(ct.test_ser_str(self.df['C']))
        self.assertTrue(ct.test_ser_str(self.df['D']))     
        self.assertFalse(ct.test_ser_str(self.df['E']))

    def test_test_ser_num(self):
        self.assertTrue(ct.test_ser_num(self.df['A']))
        self.assertTrue(ct.test_ser_num(self.df['B']))
        self.assertTrue(ct.test_ser_num(self.df['C']))
        self.assertFalse(ct.test_ser_num(self.df['D']))
        self.assertFalse(ct.test_ser_str(self.df['E']))

    def test_test_ser_int(self):
        self.assertTrue(ct.test_ser_int(self.df['A']))
        self.assertFalse(ct.test_ser_int(self.df['B']))
        self.assertFalse(ct.test_ser_int(self.df['C']))
        self.assertFalse(ct.test_ser_int(self.df['D']))
        self.assertFalse(ct.test_ser_str(self.df['E']))

    def test_test_ser_flt(self):
        self.assertFalse(ct.test_ser_flt(self.df['A']))
        self.assertTrue(ct.test_ser_flt(self.df['B']))
        self.assertFalse(ct.test_ser_flt(self.df['C']))
        self.assertFalse(ct.test_ser_flt(self.df['D']))
        self.assertFalse(ct.test_ser_str(self.df['E']))

    def test_test_ser_cmplx(self):
        self.assertFalse(ct.test_ser_cmplx(self.df['A']))
        self.assertFalse(ct.test_ser_cmplx(self.df['B']))
        self.assertTrue(ct.test_ser_cmplx(self.df['C']))
        self.assertFalse(ct.test_ser_cmplx(self.df['D']))
        self.assertFalse(ct.test_ser_str(self.df['E']))

    def test_test_ser_bool(self):
        self.assertFalse(ct.test_ser_bool(self.df['A']))
        self.assertFalse(ct.test_ser_bool(self.df['B']))
        self.assertFalse(ct.test_ser_bool(self.df['C']))
        self.assertFalse(ct.test_ser_bool(self.df['D']))
        self.assertTrue(ct.test_ser_bool(self.df['E']))
