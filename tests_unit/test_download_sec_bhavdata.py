import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from sec_bhavdata_full import download_sec_bhavdata_full 
from constants import get_sec_bhavdata_file_name
import itertools


def test_download_sec_bhavdata_full() : 
    
    date_strings = ['05042021','06042021','07042021','08042021','09042021']
    file_count, sec_bhavdata_file_names = download_sec_bhavdata_full(date_strings)
    assert file_count == 5 
    for date_string , file_name in zip(date_strings , sec_bhavdata_file_names ) : 
        assert file_name == get_sec_bhavdata_file_name(date_string) 

