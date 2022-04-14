import unittest
from unittest import result
import assign
import requests
import json
from requests.exceptions import Timeout

class TestAssign(unittest.TestCase):

    def test_perfect_square(self):
        self.assertTrue(assign.perfect_square(64),None)

    def test_check_PowerOf_4(self):
        self.assertTrue(assign.check_PowerOf_4(64),None)
    
    def test_read_data(self):
        self.assertTrue(assign.read_data(url="https://catfact.ninja/facts?limit=1&max_length=140"))

    def test_timeout_request(self):
        self.assertTrue(assign.timeout_request(url="https://uda.ke/site"))

    def test_basic_stats(self):
        result = assign.basic_stats([100, 200 ,300, 400, 500])
        self.assertTrue(result["mean"], [300])
        self.assertTrue(result["mode"], [100, 200, 300, 400, 500])
        self.assertTrue(result["variance"], [25000])
        self.assertTrue(result["median"], 300)

if __name__== '__main__':
    unittest.main()