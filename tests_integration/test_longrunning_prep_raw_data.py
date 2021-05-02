from prep_raw_data import prep_sec_bhavdata_full
import constants
import os 

def test_prep_sec_bhavdata_full_file_not_existing() : 
    date_strings = ['01012020']
    
    # Delete the files. We would like to download these. 
    for date_string in date_strings : 
        raw_file = constants.get_full_path_of_prepped_data_file(date_string)
        if os.path.isfile (raw_file) == True : 
            os.remove(raw_file)

    file_count , prep_sec_files = prep_sec_bhavdata_full( date_strings)

    assert len(date_strings) == file_count
    assert len(date_strings) == len(prep_sec_files)

def test_download_sec_bhavdata_full_raw_file_not_existing() : 
    date_strings = ['01011919']
    file_count , prep_sec_files = prep_sec_bhavdata_full( date_strings)

    assert 0 == file_count
    assert 0 == len(prep_sec_files)

