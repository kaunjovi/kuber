from reports import get_top_20_deliveries
from reports import get_top_20_deliveries_for_trade_dates
from trade_dates import fetch_trade_date_strings
import os
from socket import timeout
import pandas as pd

# def test_today() : 
#     raw_data_file_full_paths , df = get_top_20_deliveries()
#     assert len(raw_data_file_full_paths) == 1

def test_trade_day () : 
    raw_data_file_full_paths , df = get_top_20_deliveries('16042020')
    assert len(raw_data_file_full_paths) == 1
    assert len(df.index) == 20 

def test_trade_days () : 
    raw_data_file_full_paths , df = get_top_20_deliveries('16042020', '18042021', '19042020')
    assert len(raw_data_file_full_paths) == 3
    assert len(df.index) == 60 

def test_trade_days_from_dates_file () : 
    trade_date_strings = fetch_trade_date_strings('recent.dates')
    raw_data_file_full_paths , df = get_top_20_deliveries_for_trade_dates(trade_date_strings)
    assert len(raw_data_file_full_paths) == 12
    assert len(df.index) == 240 

    # print (df)

