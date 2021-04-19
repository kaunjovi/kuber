from reports import get_top_20_deliveries
import os
import pytest
from socket import timeout

###########
# These are long running tests. 
# Run these only once in a while, when getting the coverage report? 
###########

def test_valid_trade_days_but_with_missing_local_data() :
#     # We shall need some valid trade days i.e. days for which data is in URL. 
#     # However for the same, data should not be available in local. 
#     # So you shall need to delete the local file at the end of the test 
#     # to make it repeatable. 
#     # Also this will be a long running test. 
    raw_data_file_full_paths , df  = get_top_20_deliveries('11042021')
    assert len(raw_data_file_full_paths) == 1
    file = "/Users/kaunjovi/code/kuber/100_full_bhav_copy/sec_bhavdata_full_11042021.csv" 
    if os.path.isfile(file) == True : 
        os.remove()
    
def test_attempt_download_data_from_non_trade_dates() :
    try:
        get_top_20_deliveries('17041998')
    except timeout:
        pass
    else:
        raise AssertionError('Expected the thing to timeout!')
    
    # In case the file was downloaded, we need to clean it up for the next run
    file = "/Users/kaunjovi/code/kuber/100_full_bhav_copy/sec_bhavdata_full_17041998.csv"
    if os.path.isfile(file) == True : 
        os.remove(file)
    
