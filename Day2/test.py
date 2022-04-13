import unittest
import assign

class TestAssign(unittest.TestCase):

    def test_perfect_square(self):
        self.assertTrue(assign.perfect_square(64),None)

    def test_check_PowerOf_4(self):
        self.assertTrue(assign.check_PowerOf_4(64),None)










if __name__== '__main__':
    unittest.main()