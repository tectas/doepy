import unittest
from doepy3_test.build_test import TestBuildMethods
from doepy3_test.read_write_test import TestReadWriteMethods


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBuildMethods))
    suite.addTest(unittest.makeSuite(TestReadWriteMethods))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
    # unittest.main()
