# Functions used to test programs.
import math
from math import log, floor
from re import X
import requests
import json
import statistics
from requests.exceptions import Timeout

def perfect_square(number):
    root = math.sqrt(number)
    return int(root + 0.5) ** 2 == number

def check_PowerOf_4(n):
    X = log(n) / log(4)
    return X == floor(X)

def read_data(url):
    response = requests.get(url).text
    dict_data = json.loads(response)
    return dict_data

def basic_stats(num_list):
    mean_list = statistics.mean(num_list)
    mode_list = statistics.mode(num_list)
    variance_list = statistics.variance(num_list)
    median_list = statistics.median(num_list)

    dict_stats = {
        'mean':mean_list,
        'mode':mode_list,
        'variance':variance_list,
        'median':median_list
 
    }
    return dict_stats

def timeout_request(url):
    try:
        data = requests.get(url, timeout=10)
        return data.status_code
    except Timeout:
        print('Timeout has been raised.')
    