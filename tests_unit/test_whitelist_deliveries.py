import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from whitelist_deliveries import fetch_whitelist_details

# TODO : Check ticker tape 

def test_whitelist_deliveries() : 
    df = fetch_whitelist_details ( ['HDFC'], ['29042021'])
    assert len(df.index) == 1 
