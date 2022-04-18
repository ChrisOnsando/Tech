import unittest
from unittest import result
import assign

class TestAssign(unittest.TestCase):
    def test_my_array(self):
        self.assertTrue(assign.my_array())
 
    def test_month(self):
        self.assertTrue(assign.month())

if __name__== '__main__':
    unittest.main()
        


