from trade_dates import fetch_trade_date_strings
import constants 
import download_raw_data
import prep_raw_data
import filter_top_deliv
# from sec_bhavdata_full import download_sec_bhavdata_full 
# from top_delivery_files import generate_top_delivery_files
# from top_average_deliveries import generate_top_average_delivery_file
# from js_data_files import generate_js_data_files

import logging

# from whitelist_deliveries import fetch_whitelist_details



if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)

    # date_strings = ['05042021','06042021','07042021','08042021','09042021']
    date_strings = fetch_trade_date_strings('recent.dates')
    # date_strings = ['05022021', '08022021', '09022021']
    
    # prepare data 
    download_raw_data.download_sec_bhavdata_full( date_strings )
    prep_raw_data.prep_sec_bhavdata_full( date_strings )

    # Get the top delivery by lacs 
    filter_top_deliv.filter_by_deliv_lacs (date_strings)
    filter_top_deliv.filter_by_deliv_percentage (date_strings)

    # Get details of a particular group of symobls 
    white_list = constants.load_white_list_symbols() 
    filter_top_deliv.filter_by_white_list (date_strings, white_list )

    # download_sec_bhavdata_full(date_strings)

    # generate_prepped_bhavdata(date_strings)
    # generate_top_delivery_files(date_strings, 50) 
    # generate_top_average_delivery_file(date_strings)
    # fetch_whitelist_details (whitelist, date_strings)
    # generate_js_data_files(date_strings)
