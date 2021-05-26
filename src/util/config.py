import src.util as util

def get_top_del_csv_name() : 
    return '/Users/kaunjovi/code/kuber/data/401_reports/top_del.csv'

def get_top_del_js_name() : 
    return '/Users/kaunjovi/code/kuber/data/401_reports/top_del.js'

def get_bhav_url( trade_date ):
    ddmmyyyy = util.get_ddmmyyyy (trade_date)
    return 'https://archives.nseindia.com/products/content/sec_bhavdata_full_' + ddmmyyyy + '.csv' 