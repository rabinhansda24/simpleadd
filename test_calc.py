import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(calc.add(''), 0)

    def test_single_number(self):
        self.assertEqual(calc.add('5'), 5)
        self.assertEqual(calc.add('10'), 10)



if __name__ == '__main__':
    unittest.main()