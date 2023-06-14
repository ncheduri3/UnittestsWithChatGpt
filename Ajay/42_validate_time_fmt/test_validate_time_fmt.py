import unittest
from validate_time_fmt import validate_time_format


class TimeFormatTest(unittest.TestCase):
    def test_valid_time_formats(self):
        self.assertTrue(validate_time_format("10:30 am"))
        self.assertTrue(validate_time_format("9:45 am"))
        self.assertTrue(validate_time_format("12:00 pm"))
        self.assertTrue(validate_time_format("1:15 pm"))
        self.assertTrue(validate_time_format("12:15 am"))

    def test_invalid_time_formats(self):
        self.assertFalse(validate_time_format("13:00 am"))
        self.assertFalse(validate_time_format("9:60 pm"))
        self.assertFalse(validate_time_format("00:00 am"))
        self.assertFalse(validate_time_format("05:00 pm"))
        self.assertFalse(validate_time_format("10:30pm"))
        self.assertFalse(validate_time_format("8:45 PM"))
        self.assertFalse(validate_time_format("1:15 BM"))


if __name__ == '__main__':
    unittest.main()
