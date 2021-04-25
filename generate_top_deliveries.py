import logging
import os.path
from constants import CONSTANTS
from constants import get_full_path_of_raw_data_file

def top_delivery_report_does_not_exist (date_string) : 
    return True

def confirmed_top_deliery_report_file_name( date_string ) : 
    return ''

def count_of_rows_in_top_deliveries_file (date_string) : 
    return 0 

def generate_top_deliveries_forced ( date_string , top ) : 
    logging.debug(f'Attempting to generate top deliveries file.')

    raw_data_file_full_path = get_full_path_of_raw_data_file(date_string)
    if os.path.isfile(raw_data_file_full_path) == False :
        logging.debug(f'Raw file does not exist {raw_data_file_full_path}')
        logging.debug(f'Download raw data and then attempt to create report')
        return 0, ''

    top_deliveries_file_name = CONSTANTS()['top_daily_folder'] + CONSTANTS()['top_daily_file'] + date_string + '.csv' 

    if os.path.isfile(top_deliveries_file_name) == False :
        logging.debug(f'Does not exist {top_deliveries_file_name}')
        logging.debug(f'We will create a new one.')
    else : 
        logging.debug(f'This one exists {top_deliveries_file_name}')
        logging.debug(f'We will overwrite one.')

    



    return 0, ''


def generate_top_deliveries( date_string , top ) : 

    top_deliveries_file_name = ''
    top_deliveries_file_line_count = 0 

    top_deliveries_file_name = confirmed_top_deliery_report_file_name(date_string)
    if len(top_deliveries_file_name.strip ( date_string))==0 : 
        logging.debug(f'Top delivery report does NOT exist for {date_string}')
        top_deliveries_file_line_count, top_deliveries_file_name = generate_top_deliveries_forced (date_string, top )

    top_deliveries_file_line_count = count_of_rows_in_top_deliveries_file (date_string)
    if  top_deliveries_file_line_count != top : 
        logging.debug(f'Top delivery report contains {top_deliveries_file_line_count} lines. It should contain {top} lines.')
    

    return top_deliveries_file_line_count, top_deliveries_file_name

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    generate_top_deliveries('05042021' , 20) 