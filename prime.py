import unittest

def check_is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestCheckIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in primes:
            self.assertTrue(check_is_prime(prime), f"{prime} should be prime")

    def test_non_prime_numbers(self):
        non_primes = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for non_prime in non_primes:
            self.assertFalse(check_is_prime(non_prime), f"{non_prime} should not be prime")

    def test_negative_number(self):
        negative_number = -7
        self.assertFalse(check_is_prime(negative_number), f"{negative_number} should not be prime")

    def test_zero(self):
        zero = 0
        self.assertFalse(check_is_prime(zero), f"{zero} should not be prime")

    def test_one(self):
        one = 1
        self.assertFalse(check_is_prime(one), f"{one} should not be prime")

if __name__ == '__main__':
    unittest.main()
