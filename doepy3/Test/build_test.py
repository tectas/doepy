import unittest
from doepy3.build import *


class TestBuildMethods(unittest.TestCase):

    def setUp(self):
        self.d = {'Pressure': [50, 60, 70], 'Temperature': [290, 320, 350], 'Flow rate': [0.9, 1.0, 1.1], 'Time': [5, 8, 11]}

    def test_full_fact(self):
        result = full_fact(self.d)
        self.assertIsNotNone(result)

    def test_frac_fact_res(self):
        result = frac_fact_res(self.d)
        self.assertIsNotNone(result)

    def test_plackett_burman(self):
        result = plackett_burman(self.d)
        self.assertIsNotNone(result)

    def test_sukharev(self):
        result = sukharev(self.d, num_samples=10)
        self.assertIsNotNone(result)

    def test_box_behnken(self):
        result = box_behnken(self.d)
        self.assertIsNotNone(result)

    def test_central_composite(self):
        result = central_composite(self.d, center=(1, 1))
        self.assertIsNotNone(result)

    def test_lhs(self):
        result = lhs(self.d)
        self.assertIsNotNone(result)

    def test_space_filling_lhs(self):
        result = space_filling_lhs(self.d)
        self.assertIsNotNone(result)

    def test_random_k_means(self):
        result = random_k_means(self.d, num_samples=8)
        self.assertIsNotNone(result)

    def test_maximin(self):
        result = maximin(self.d)
        self.assertIsNotNone(result)

    def test_halton(self):
        result = halton(self.d, num_samples=10)
        self.assertIsNotNone(result)

    def test_uniform_random(self):
        result = uniform_random(self.d, num_samples=12)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
