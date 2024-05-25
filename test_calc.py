import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(calc.add(''), 0)

    def test_single_number(self):
        self.assertEqual(calc.add('5'), 5)
        self.assertEqual(calc.add('10'), 10)
    
    def test_two_numbers(self):
        self.assertEqual(calc.add('1,2'), 3)
        self.assertEqual(calc.add('10,20'), 30)
    
    def test_multiple_numbers(self):
        self.assertEqual(calc.add('1,2,3,4,5'), 15)
        self.assertEqual(calc.add('10,20,30,40,50'), 150)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            calc.add('1,-2,3,-4,5')
        self.assertEqual(str(context.exception), 'Negatives not allowed')

    def test_new_lines_between_numbers(self):
        self.assertEqual(calc.add('1\n2,3'), 6)
        self.assertEqual(calc.add('10\n20,30'), 60)



if __name__ == '__main__':
    unittest.main()