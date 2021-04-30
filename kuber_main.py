from sec_bhavdata_full import download_sec_bhavdata_full 
from top_delivery_files import generate_top_delivery_files
from top_average_deliveries import generate_top_average_delivery_file
from js_data_files import generate_js_data_files
from trade_dates import fetch_trade_date_strings
# from whitelist_deliveries import fetch_whitelist_details

if __name__ == "__main__":
    # date_strings = ['05042021','06042021','07042021','08042021','09042021']
    date_strings = fetch_trade_date_strings('recent.dates')
    download_sec_bhavdata_full(date_strings)
    generate_top_delivery_files(date_strings, 50) 
    generate_top_average_delivery_file(date_strings)
    # fetch_whitelist_details (whitelist, date_strings)
    generate_js_data_files(date_strings)

