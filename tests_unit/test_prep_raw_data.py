from prep_raw_data import prep_sec_bhavdata_full
import os 

def test_download_sec_bhavdata_full() : 
    date_strings = ['01012020']
    file_count , prep_sec_files = prep_sec_bhavdata_full( date_strings)

    assert len(date_strings) == file_count
    assert len(date_strings) == len(prep_sec_files)
