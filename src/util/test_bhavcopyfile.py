import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import src.util as util

def test_get_bhav_file_name() : 
    bhav_file_name = util.get_bhav_file_name()
    assert bhav_file_name== '/Users/kaunjovi/code/kuber/data/100_full_bhav_copy/sec_bhavdata_full_26052021.csv'