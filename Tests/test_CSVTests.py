import unittest
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('./Tests/Data/unit_test_sample_mean.csv')

    def test_get_data(self):
        self.assertGreaterEqual(len(self.csv_reader.data),1)
        self.assertIn("nums",self.csv_reader.data[0])
        self.assertIn("result",self.csv_reader.data[0])
        self.assertEqual(self.csv_reader.data[0]["nums"],"500_700_900")
        self.assertEqual(self.csv_reader.data[0]["result"],"700")
        self.assertEqual(self.csv_reader.data[1]["nums"],"50_100")
        self.assertEqual(self.csv_reader.data[1]["result"],"75")

if __name__ == '__main__':
    unittest.main()
