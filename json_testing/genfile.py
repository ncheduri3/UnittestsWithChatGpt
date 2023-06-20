import unittest

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


class TestClass(unittest.TestCase):
    def test_heapify(self):
        # Test case with an unsorted array
        arr = [4, 10, 3, 5, 1]
        n = len(arr)
        i = 0

        heapify(arr, n, i)

        # After heapify, the expected output should be [10, 5, 3, 4, 1]
        expected_output = [10, 5, 3, 4, 1]

        self.assertEqual(arr, expected_output)

    def test_heapify_already_heap(self):
        # Test case with an already max heap array
        arr = [10, 5, 3, 4, 1]
        n = len(arr)
        i = 0

        heapify(arr, n, i)

        # The array should remain unchanged
        expected_output = [10, 5, 3, 4, 1]

        self.assertEqual(arr, expected_output)

    def test_heapify_empty_array(self):
        # Test case with an empty array
        arr = []
        n = len(arr)
        i = 0

        heapify(arr, n, i)

        # The array should remain empty
        expected_output = []

        self.assertEqual(arr, expected_output)

    def test_heapify_single_element(self):
        # Test case with a single-element array
        arr = [5]
        n = len(arr)
        i = 0

        heapify(arr, n, i)

        # The array should remain unchanged
        expected_output = [5]

        self.assertEqual(arr, expected_output)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("PASS")
