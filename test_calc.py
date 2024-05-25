import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(calc.add(''), 0)



if __name__ == '__main__':
    unittest.main()