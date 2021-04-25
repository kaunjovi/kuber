from sec_bhavdata_full import download_sec_bhavdata_full 
from util import get_sec_bhavdata_file_name
import itertools


def test_download_sec_bhavdata_full() : 
    
    date_strings = ['05042021','06042021','07042021','08042021','09042021']
    file_count, sec_bhavdata_file_names = download_sec_bhavdata_full(date_strings)
    assert file_count == 5 
    for date_string , file_name in zip(date_strings , sec_bhavdata_file_names ) : 
        assert file_name == get_sec_bhavdata_file_name(date_string) 

def test_download_sec_bhavdata_full_non_existent_url() : 
    
    date_strings = ['24042021']
    file_count, sec_bhavdata_file_names = download_sec_bhavdata_full(date_strings)
    assert file_count == 0
    assert len(sec_bhavdata_file_names) == 0  
    # for date_string in date_strings : 
    #     for file_name in sec_bhavdata_file_names : 
    #         assert file_name == get_sec_bhavdata_file_name(date_string) 

