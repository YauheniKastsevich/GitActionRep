import unittest

class BasicCalculationTestCase(unittest.TestCase):
    def test_sum(self):
        a = 5
        b = 10
        result = a + b
        self.assertEqual(result, 15)

if __name__ == "__main__":
    unittest.main()
