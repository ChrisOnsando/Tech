import unittest
from unittest import result
import assign

class TestAssign(unittest.TestCase):
    def test_convert(self):
        self.assertTrue(assign.convert(self,'USD','KES','amount'))

if __name__== '__main__':
    unittest.main()