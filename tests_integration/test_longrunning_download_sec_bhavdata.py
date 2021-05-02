import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from sec_bhavdata_full import download_sec_bhavdata_full 
from constants import get_sec_bhavdata_file_name
import itertools


def test_download_sec_bhavdata_from_web() : 
    
    # try to download something that exists in the web
    # but does not on the local
    date_strings = ['01102019']
    file_count, sec_bhavdata_file_names = download_sec_bhavdata_full(date_strings)
    assert file_count == 1 
    for date_string , file_name in zip(date_strings , sec_bhavdata_file_names ) : 
        assert file_name == get_sec_bhavdata_file_name(date_string) 
        # at the end, we want to delete the file 
        # so the test is repeatable. 
        os.remove(file_name)

def test_download_non_existent_sec_bhavdata() : 
    
    # try to download something that exists in the web
    # but does not on the local
    date_strings = ['01101919']
    file_count, sec_bhavdata_file_names = download_sec_bhavdata_full(date_strings)
    assert file_count == 0 



