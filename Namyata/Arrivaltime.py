def findDelayedArrivalTime( arrivalTime: int, delayedTime: int) -> int:
    return (arrivalTime + delayedTime) % 24


import unittest


class TestFindDelayedArrivalTime(unittest.TestCase):

    def test_find_delayed_arrival_time(self):
    # Replace YourClass with the actual class name

        # Test Case 1
        self.assertEqual(findDelayedArrivalTime(10, 5), 15)

        # Test Case 2
        self.assertEqual(findDelayedArrivalTime(20, 8), 4)

        # Test Case 3
        self.assertEqual(findDelayedArrivalTime(5, 20), 1)

        # Test Case 4
        self.assertEqual(findDelayedArrivalTime(15, 0), 15)

        # Test Case 5
        self.assertEqual(findDelayedArrivalTime(23, 3), 2)


if __name__ == '__main__':
    unittest.main()


## All test cases given out by chat gpt are fine.

# Question : - You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive integer delayedTime denoting the amount of delay in hours.
#
# Return the time when the train will arrive at the station.
#
# Note that the time in this problem is in 24-hours format.