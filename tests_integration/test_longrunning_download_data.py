from download_data import download_sec_bhavdata_full 
import os 
import constants


def test_download_sec_bhavdata_full_url_existing_file_not() : 
    date_strings = ['01012020']
    
    # Delete the files. We would like to download these. 
    for date_string in date_strings : 
        raw_file = constants.get_full_path_of_raw_data_file(date_string)
        if os.path.isfile (raw_file) == True : 
            os.remove(raw_file)

    file_count , sec_bhavdata_full = download_sec_bhavdata_full( date_strings)

    assert len(date_strings) == file_count
    assert len(date_strings) == len(sec_bhavdata_full)

def test_download_sec_bhavdata_full_not_existing_url() : 
    date_strings = ['01011919']
    file_count , sec_bhavdata_full = download_sec_bhavdata_full( date_strings)

    assert 0 == file_count
    assert 0 == len(sec_bhavdata_full)

