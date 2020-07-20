import unittest

def suma(num1, num2):
    return num1 + num2

class CajaNegraTest(unittest.TestCase):
    def test_two_positives_sum(self):
        num1 = 10
        num2 = 15
        result = suma(num1, num2)
        self.assertEqual(result, 25)
    
    def test_two_negatives_sum(self):
        num1 = -10
        num2 = -7
        result = suma(num1, num2)
        self.assertEqual(result, -17)

if __name__ == "__main__":
    unittest.main(verbosity=2)
