import unittest
import assign

class TestforValues(unittest.TestCase):
    #test that the sentence cannot be empty
    def test_sentence(self):
        self.assertIsNotNone(assign.sentence)
# test that the sentence has to be a string
class TestForType(unittest.TestCase):
    def test_sentence(self):
        self.assertIsInstance(assign.sentence, str)


if __name__ == '__main__':
       unittest.main()