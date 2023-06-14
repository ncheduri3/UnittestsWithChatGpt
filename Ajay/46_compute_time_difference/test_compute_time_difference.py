import unittest
from compute_time_difference import compute_time_difference


class TimeDifferenceTestCase(unittest.TestCase):
    def test_compute_time_difference(self):
        time1 = "10:30:00 am"
        time2 = "02:45:15 pm"
        self.assertEqual(compute_time_difference(time1, time2), "04:15:15")
        
        time1 = "11:59:00 pm"
        time2 = "12:01:00 am"
        self.assertEqual(compute_time_difference(time1, time2), "00:02:00")
        
        time1 = "05:15:45 pm"
        time2 = "05:15:45 pm"
        self.assertEqual(compute_time_difference(time1, time2), "00:00:00")
        
        time1 = "09:00:00 am"
        time2 = "09:00:30 am"
        self.assertEqual(compute_time_difference(time1, time2), "00:00:30")
        
        time1 = "12:00:00 pm"
        time2 = "12:00:00 am"
        self.assertEqual(compute_time_difference(time1, time2), "12:00:00")
        
        time1 = "03:43:23 pm"
        time2 = "03:43:23 pm"
        self.assertEqual(compute_time_difference(time1, time2), "00:00:00")


if __name__ == '__main__':
    unittest.main()
