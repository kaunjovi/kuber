from trade_dates import fetch_trade_date_strings 

def test_list_of_recent_dates(): 
    trade_date_strings = fetch_trade_date_strings('recent.dates')
    assert len(trade_date_strings) == 12 