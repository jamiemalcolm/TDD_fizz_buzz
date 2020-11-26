import unittest

from src.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz__3_returns_fizz(self):
        self.assertEqual("fizz", fizz_buzz(3))

    def test_fizz_buzz__6_returns_fizz(self):
        self.assertEqual("fizz", fizz_buzz(6))

    def test_fizz_buzz__5__returns_buzz(self):
        self.assertEqual("buzz", fizz_buzz(5))

    def test_fizz_buzz__15__returns_fizzbuzz(self):
        self.assertEqual("fizzbuzz", fizz_buzz(15))

    def test_fizz_buzz__4_returns_4_as_str(self):
        self.assertEqual("4", fizz_buzz(4))

    def test_fizz_buzz__10__returns_buzz(self):
        self.assertEqual("buzz", fizz_buzz(10))
