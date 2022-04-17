from numpy import number
import assign
import unittest

class TestAssign(unittest.TestCase):
    def test_my_greeting(self):
        self.assertTrue(assign.my_greeting("name", "msg", "sendoff"))

    def test_my_function(self):
        self.assertTrue(assign.my_function())

    def test_my_number(self):
        self.assertTrue(assign.my_number())

    def test_add_fish_to_aquarium(self):
        self.assertTrue(assign.add_fish_to_aquarium())

if __name__== '__main__':
    unittest.main()