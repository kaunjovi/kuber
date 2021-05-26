import logging
import src.util as util
import src.bhavcopyfile as bhav
import src.reports as reports


# Generate daily reports. 
# Report 1 - Delivery details of the tickers of interest, WHITELIST
#  

if __name__ == "__main__":
    logging.basicConfig(format='%(filename)s.%(funcName)s().%(lineno)s $$ %(message)s', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)

    trade_dates = util.load_trade_dates() 

    logging.debug(f'Running EOD process for {len(trade_dates)} day(s).')

# Step 1 - Get the raw files. 
    trade_dates, bhav_files, bhav_files_new = bhav.download(trade_dates)
    logging.debug(f'Downloaded {len(bhav_files_new)} files. Now {len(bhav_files)} are available.')

# Step 2 - Prep the raw files for analysis 
    trade_dates, prepped_bhav_files, prepped_bhav_files_new = bhav.prep_for_analysis(trade_dates)
    logging.debug(f'{len(prepped_bhav_files)} prepped files available for analysis.')
    logging.debug(f'{len(prepped_bhav_files_new)} created new.')

# Step 3 - Pull delivery figures of interest 
    top_daily_delivery_files = bhav.fetch_top_deliveries( trade_dates )

# Step 4 - Generate the report files. 
    reports.generate_top_del_report(trade_dates) 
    




    