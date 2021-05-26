import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import src.util as util

def test_gen_bhav_file_names() : 
    bhav_files_to_download = util.gen_bhav_file_names()
    assert len(bhav_files_to_download) == 1 
    assert bhav_files_to_download[0]== '/Users/kaunjovi/code/kuber/data/100_full_bhav_copy/sec_bhavdata_full_26052021.csv'