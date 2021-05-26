import logging
import src.util as util
import src.bhavcopyfile as bhav


# Generate daily reports. 
# Report 1 - Delivery details of the tickers of interest, WHITELIST
#  

if __name__ == "__main__":
    logging.basicConfig(format='%(filename)s.%(funcName)s().%(lineno)s $$ %(message)s', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)

    trade_dates = util.load_trade_dates() 

    logging.debug(f'Running EOD process for {len(trade_dates)} day(s).')

    bhav_files, fresh_bhav_files = bhav.download(trade_dates)
    logging.debug(f'Downloaded {len(fresh_bhav_files)} files. Now {len(bhav_files)} are available.')

    prepped_bhav_files, prepped_bhav_files_new = bhav.prep_for_analysis(bhav_files)
    logging.debug(f'{len(prepped_bhav_files)} prepped files available for analysis. {len(prepped_bhav_files_new)} created new.')

    