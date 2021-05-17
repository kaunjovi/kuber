import trade_dates 
import constants 
import download_sec_bhav_data
import prep_sec_bhav_data
import filter_top_deliv
# from sec_bhavdata_full import download_sec_bhavdata_full 
# from top_delivery_files import generate_top_delivery_files
# from top_average_deliveries import generate_top_average_delivery_file
# from js_data_files import generate_js_data_files

import logging

# from whitelist_deliveries import fetch_whitelist_details

if __name__ == "__main__":

    logging.basicConfig(format='%(filename)s.%(funcName)s().%(lineno)s $$ %(message)s', level=logging.DEBUG)

    # Pull some trade dates to run the process on. 
    # date_strings = ['05022021', '08022021', '09022021']
    # date_strings = ['05042021','06042021','07042021','08042021','09042021']
    date_strings = trade_dates.load_file('recent.dates')
    
    # Download sec bhav data and prep for analysis 
    download_sec_bhav_data.for_dates( date_strings )
    prep_sec_bhav_data.for_dates( date_strings )

    # Get the top delivery by lacs 
    filter_top_deliv.filter_by_deliv_lacs (date_strings)
    filter_top_deliv.filter_by_deliv_percentage (date_strings)

    # Get details of a particular group of symobls 
    white_list = constants.load_white_list_symbols() 
    filter_top_deliv.filter_by_white_list (date_strings, white_list )
    # filter_top_deliv.filter_by_white_list (date_strings, ['HDFCBANK', 'ICICIBANK', 'KOTAKBANK'] )

    # download_sec_bhavdata_full(date_strings)

    # generate_prepped_bhavdata(date_strings)
    # generate_top_delivery_files(date_strings, 50) 
    # generate_top_average_delivery_file(date_strings)
    # fetch_whitelist_details (whitelist, date_strings)
    # generate_js_data_files(date_strings)
