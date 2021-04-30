import logging
import pandas as pd 
from constants import get_sec_bhavdata_file_name
from top_delivery_files import scrub_raw_bhav_copy_df
from trade_dates import fetch_trade_date_strings
from util_bhav_file import prep_raw_bhv_data_for_analysis
    
def fetch_whitelist_details ( tickers , dates ) : 

    # Iterate over the dates 
    # from the raw data files 
    # fetch the details of each of the tickers 
    # put them into dataframes 
    # and then stitch them into a big data frame
    # return back the dataframe 
    dfs = []

    for date in dates : 
        raw_data_file = get_sec_bhavdata_file_name(date)
        logging.debug(f'Data for {date} is {raw_data_file} ')
        
        df = pd.read_csv(raw_data_file)
        df = prep_raw_bhv_data_for_analysis( df )

        # Pick only the data for whitelisted tickers. 
        df = df[df.SYMBOL.isin(tickers)]

        dfs.append(df)


    return pd.concat(dfs, ignore_index=True) 

# prp whitelist_deliveries.py
# pipenv run coverage run --source=. -m pytest unit_tests/test_whitelist_deliveries.py ; pipenv run coverage html

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)

    # df = fetch_whitelist_details ( ['HDFC'], ['29042021'])
    # logging.debug(f'Fetched {len(df.index)} records')
    # logging.debug(f'{df.head()}')

    # df = fetch_whitelist_details ( ['HDFC', 'RELAXO'], ['28042021','29042021'])
    # logging.debug(f'Fetched {len(df.index)} records')
    # logging.debug(f'{df.head()}')

    # dates = fetch_trade_date_strings('recent.dates')
    # df = fetch_whitelist_details ( ['LALPATHLAB'], dates)
    # logging.debug(f'Fetched {len(df.index)} records')
    # logging.debug(f'{df.head(30)}')