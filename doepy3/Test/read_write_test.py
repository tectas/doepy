import unittest
import pandas as pd
from doepy3.read_write import read_variables_csv, write_csv, write_json, read_json


class TestReadWriteMethods(unittest.TestCase):

    def setUp(self):
        self.data = {'Pressure': [40, 55, 70], 'Temperature': [290, 320, 350], 'FlowRate': [0.2, 0.3, 0.4],
                     "Time": [5, 8, 11]}
        self.df = pd.DataFrame(self.data)
        self.filename_csv = '../Data/params.csv'
        self.filename_json = '../Data/params.json'

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
