from download_data import download_sec_bhavdata_full 
import os 
import constants

def test_download_sec_bhavdata_full() : 
    date_strings = ['01012020']
    file_count , sec_bhavdata_full = download_sec_bhavdata_full( date_strings)

    assert len(date_strings) == file_count
    assert len(date_strings) == len(sec_bhavdata_full)
