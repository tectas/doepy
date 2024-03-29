import unittest
import pandas as pd

from doepy3_test.test_environment import ReadWriteTestData as TestData
from doepy3.read_write import read_variables_csv, write_csv, write_json, read_json


class TestReadWriteMethods(unittest.TestCase):

    def setUp(self):
        self.data = TestData.TEST_DATA
        self.df = pd.DataFrame(self.data)
        self.filename_csv = TestData.CSV_PATH
        self.filename_json = TestData.JSON_PATH

    def test_read_variables_csv(self):
        result = read_variables_csv(self.filename_csv)
        self.assertEqual(result, self.data)

    def test_write_csv(self):
        write_csv(self.df, self.filename_csv)
        read_result = read_variables_csv(self.filename_csv)
        self.assertEqual(read_result, self.data)

    def test_read_json(self):
        result = read_json(self.filename_json)
        self.assertEqual(result, self.data)

    def test_write_json(self):
        write_json(self.df, self.filename_json)
        read_result = read_json(self.filename_json)
        self.assertEqual(read_result, self.data)


if __name__ == '__main__':
    unittest.main()
