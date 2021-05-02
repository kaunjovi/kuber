import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from bhav_data import generate_analysis_ready_bhavdata
import constants 

def test_generate_analysis_ready_bhavdata() : 

    date_strings = ['01012020']

    # Check if raw file exists for all the dates 
    raw_data_file_count = 0  
    for date_string in date_strings : 
        if os.path.isfile( constants.get_sec_bhavdata_file_name(date_string) ) == True : 
            raw_data_file_count +=1 
    
    assert len(date_strings) == raw_data_file_count
    

    generate_analysis_ready_bhavdata( date_strings)
    assert False 
