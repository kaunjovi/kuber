from datetime import date
import logging
import os.path
import urllib.request
from urllib.error import HTTPError, URLError
from socket import timeout
import shutil
from download_raw_data import get_full_path_of_raw_data_file
from download_raw_data import download_data_for_date_string

def extract_date_strings_from_parameters( args ) : 
    date_strings = [] 

    if len(args) == 0 : 
    # if no date were passed as an argument, 
    # attempt to get top 20 delivereis for today. 
        date_strings.append(date.today().strftime('%d%m%Y'))
    else : 
        date_strings.extend(list(args))

    return date_strings

def fetch_raw_data_file_full_paths(date_strings) : 

    raw_data_file_full_paths = []

    for date_str in date_strings : 
        logging.debug(f'Get top 20 deliveries for {date_str} ')

        raw_data_file_full_path = get_full_path_of_raw_data_file(date_str)
        
        if os.path.isfile(raw_data_file_full_path) == False :
            download_data_for_date_string (date_str)

        if os.path.isfile(raw_data_file_full_path) == True : 
            logging.debug(f'{raw_data_file_full_path} was found. Adding it now.')
            raw_data_file_full_paths.append( raw_data_file_full_path)


    return raw_data_file_full_paths 


def get_top_20_deliveries (*args , **kwds) : 

    date_strings = extract_date_strings_from_parameters(args) 

    raw_data_file_full_paths = fetch_raw_data_file_full_paths(date_strings)

    logging.debug(f'Reading data from {len(raw_data_file_full_paths)} files.')

    return raw_data_file_full_paths

# if __name__ == "__main__":
#     # run the code for today.
#     get_top_20_deliveries()

#     # logging.basicConfig(level=logging.DEBUG)
#     # get_top_20_deliveries('15042021', '13042021')
#     # get_top_20_deliveries('15042021')
#     # get_top_20_deliveries('15042020')
#     # get_top_20_deliveries('14042021', '15042021', '17042021', '16042021', '18042021' )