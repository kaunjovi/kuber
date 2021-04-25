import os.path
import logging
from util import get_sec_bhavdata_file_name
from util import get_sec_bhavdata_url
from download_data_from_web import download_from_url_to_file


# file_count - number of files that are there in the folder after running this def
# sec_bhavdata_file_names - full path of the files. 
def download_sec_bhavdata_full (date_strings ): 
    file_count = 0 
    sec_bhavdata_file_names = []

    for date_string in date_strings : 
        if os.path.isfile(get_sec_bhavdata_file_name(date_string)) == True :
            logging.debug(f'Found {get_sec_bhavdata_file_name(date_string)} locally.')
            file_count += 1 
            sec_bhavdata_file_names.append(get_sec_bhavdata_file_name(date_string))
        else :
            logging.debug(f'Did not find {get_sec_bhavdata_file_name(date_string)} locally.')
            try : 
                download_from_url_to_file ( get_sec_bhavdata_url(date_string), get_sec_bhavdata_file_name(date_string))
                file_count += 1 
                sec_bhavdata_file_names.append(get_sec_bhavdata_file_name(date_string))
                logging.debug(f'Downloaed {get_sec_bhavdata_file_name(date_string)} locally.')
            except : 
                logging.debug(f'Could not download from {get_sec_bhavdata_url(date_string)}')
            # Write code to download the file. 
            # Also, if the file could not be downloaded, handle that. 

    
        
    return file_count, sec_bhavdata_file_names


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    date_strings = ['05042021','06042021','07042021','08042021','09042021']
    # date_strings = ['24042021']
    file_count, sec_bhavdata_file_names = download_sec_bhavdata_full(date_strings)
    for f in sec_bhavdata_file_names : 
        print(f'{f}')