import unittest

import pandas
import numpy
import random

from doepy3.build import *
from doepy3_test.test_environment import FunctionsTestData as TestData


class TestBuildMethods(unittest.TestCase):

    def setUp(self):
        self.data = TestData.TEST_DATA
        numpy.random.seed(0)
        random.seed(0)

    def test_full_fact(self):
        result = full_fact(self.data)
        expected = TestData.FULL_FRACT_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_frac_fact_res(self):
        result = frac_fact_res(self.data, 2)
        expected = TestData.FULL_FRACT_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_plackett_burman(self):
        result = plackett_burman(self.data)
        expected = TestData.PLACKETT_BURMAN_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_sukharev(self):
        result = sukharev(self.data, TestData.SUKHAREV_SAMPLE_COUNT)
        expected = TestData.SUKHAREV_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_box_behnken(self):
        result = box_behnken(self.data)
        expected = TestData.BOX_BEHNKEN_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_central_composite(self):
        result = central_composite(self.data, TestData.CENTER_COMPOSITE_CENTER)
        expected = TestData.CENTRAL_COMPOSITE_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_lhs(self):
        result = lhs(self.data, random_state=0)
        expected = TestData.LHS_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_space_filling_lhs(self):
        result = space_filling_lhs(self.data)
        expected = TestData.SPACE_FILLING_LHS_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_random_k_means(self):
        result = random_k_means(self.data, TestData.RANDOM_K_MEANS_SAMPLE_COUNT)
        expected = TestData.RANDOM_K_MEANS_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_maximin(self):
        result = maximin(self.data)
        expected = TestData.MAXIMIN_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_halton(self):
        result = halton(self.data, TestData.HALTON_SAMPLE_COUNT)
        expected = TestData.HALTON_TEST_RESULT
        pandas.testing.assert_frame_equal(result, expected)

    def test_uniform_random(self):
        result = uniform_random(self.data, TestData.UNIFORM_RANDOM_SAMPLE_COUNT)
        expected = TestData.UNIFORM_RANDOM_RESULT
        pandas.testing.assert_frame_equal(result, expected)


if __name__ == '__main__':
    unittest.main()
