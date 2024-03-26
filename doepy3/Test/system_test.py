import unittest
from doepy3.Test.build_test import TestBuildMethods
from doepy3.Test.read_write_test import TestReadWriteMethods


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBuildMethods))
    suite.addTest(unittest.makeSuite(TestReadWriteMethods))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
