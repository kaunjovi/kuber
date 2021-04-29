import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from sec_bhavdata_full import download_sec_bhavdata_full 
from top_delivery_files import generate_top_delivery_files
from top_average_deliveries import generate_top_average_delivery_file

from constants import get_sec_bhavdata_file_name
from constants import get_top_delivery_file_name
from constants import get_top_average_delivery_file_name

import itertools


def test_kuber_main() : 

    # date_strings = ['05042021','06042021','07042021','08042021','09042021']
    date_strings = ['05042021']
    
    file_count, sec_bhavdata_file_names = download_sec_bhavdata_full(date_strings)
    assert file_count == 1 
    for date_string , file_name in zip(date_strings , sec_bhavdata_file_names ) : 
        assert file_name == get_sec_bhavdata_file_name(date_string) 

    file_count, file_names = generate_top_delivery_files(date_strings, 100)
    assert file_count == 1 
    for date_string , file_name in zip(date_strings , file_names ) : 
        assert file_name == get_top_delivery_file_name(date_string) 

    row_count, file_name = generate_top_average_delivery_file(date_strings)
    assert row_count == 100 
    assert file_name == get_top_average_delivery_file_name
    
