import unittest

def has_legal_age(age):
    if(age >= 18):
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    def test_is_adult(self):
        age = 20
        result = has_legal_age(age)
        self.assertEqual(result, True)
    
    def test_is_child(self):
        age = 5
        result = has_legal_age(age)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main(verbosity=2)
