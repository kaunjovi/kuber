import os
import logging
import pandas as pd 
from  constants import get_top_delivery_file_name
from  constants import get_sec_bhavdata_file_name
from util_bhav_file import prep_raw_bhv_data_for_analysis


def calculate_top_delivery( filename , top ) : 
    df = pd.read_csv(filename)
    df = prep_raw_bhv_data_for_analysis(df)
    return df.head(top) 


# ip
# date_strings - the dates for which to calculat the top deliveris and create file. 
# top - how many on top to calulate
# op 
def generate_top_delivery_files(date_strings, top) : 

    file_count = 0 
    top_delivery_file_names = []

    for date_string in date_strings : 

        # If the top delivery files are already there, then delete them 
        # We need clean directory 
        if os.path.isfile(get_top_delivery_file_name(date_string)) == True :
            logging.debug(f'{get_top_delivery_file_name(date_string)} exists. Deleting old. Creating new.')
            os.remove(get_top_delivery_file_name(date_string))
        else : 
            logging.debug(f'{get_top_delivery_file_name(date_string)} does not exist. Creating one now.')

        # If raw data file is present offline, create the top delivery file. 
        # Else, dont try to download raw file here. Just report that and move on. 
        if os.path.isfile(get_sec_bhavdata_file_name(date_string)) == True :
            df = calculate_top_delivery( get_sec_bhavdata_file_name(date_string), top )
            df.to_csv(get_top_delivery_file_name(date_string), index = False, header=True)
            # logging.debug(df)
            top_delivery_file_names.append(get_top_delivery_file_name(date_string))
            file_count += 1 
        else : 
            logging.debug(f'Did not find {get_sec_bhavdata_file_name(date_string)}. Not attempting auto fix. Check manually please.')
        
    return file_count, top_delivery_file_names

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)
#     date_strings = ['05042021','06042021','07042021','08042021','09042021']
#     # date_strings = ['24042021']
#     file_count, top_delivery_file_names = generate_top_delivery_files(date_strings, 100)
#     for f in top_delivery_file_names : 
#         print(f'{f}')
