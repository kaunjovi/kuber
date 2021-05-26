import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../.."))

import src.util as util

def test_load_trade_dates() : 
    trade_dates = util.load_trade_dates() 
    assert len(trade_dates) == 1 
