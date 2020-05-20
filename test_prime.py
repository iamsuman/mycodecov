import unittest
# import mock

from prime import prime_test


class Testmyprime(unittest.TestCase):
    def test_prime_test_1(self):
        assert prime_test(1) == False

    def test_prime_test_2(self):
        assert prime_test(2) == True

    def test_prime_test_3(self):
        assert prime_test(23) == True

    def test_prime_test_4(self):
        assert prime_test(49) == False

    def test_prime_test_5(self):
        assert prime_test(8) == False






