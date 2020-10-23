#!python3
# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../'))

import unittest
import numpy as np
from taylorseries import taylorseries as ts


######################################################
# Test Cases
######################################################
class TestTaylor(unittest.TestCase):

    def setUp(self):
        self.xs = np.array([1,2,3])
        self.ys = np.array([1,4,9])

        temp = [[1,1,1],
                [1,2,4],
                [1,3,9]]

        self.X = np.array(temp)

    def tearDown(self):
        pass


    def test_gen_matrix_X(self):

        temp = ts.gen_matrix_X(self.xs)
        self.assertTrue((temp==self.X).all(),
                        "Generate matrix X incorrect\ninput xs: {}\ngen_matrix_X:\n{};\ntest matrix:\n{}".format(self.xs,temp,self.X))


######################################################
# Test Suite
######################################################
def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestTaylor("test_gen_matrix_X"))

    return suite


######################################################
# main
######################################################
def _main_():
    unittest.main()

    # runnner to run all test suites in a file
    # runner = unittest.TextTestRunner()
    # runner.run(suite())

if __name__ == "__main__":
    _main_()