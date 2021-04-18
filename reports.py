from datetime import date
import logging
import os.path

def get_raw_data_file_full_path ( date_string) : 
    return "/Users/kaunjovi/code/kuber/100_full_bhav_copy/" + 'sec_bhavdata_full_' + date_string + '.csv'

def get_top_20_deliveries (*args , **kwds) : 
    date_strings = [] 

    if len(args) == 0 : 
    # if no date were passed as an argument, 
    # attempt to get top 20 delivereis for today. 
        date_strings.extend(date.today().strftime('%d%m%Y'))
    else : 
        date_strings.extend(list(args))

    raw_data_file_full_paths = []

    for date_str in date_strings : 
        logging.debug(f'Get top 20 deliveries for {date_str} ')

        raw_data_file_full_path = get_raw_data_file_full_path(date_str)
        if os.path.isfile(raw_data_file_full_path) == True : 
            logging.debug(f'{raw_data_file_full_path} exists')
            raw_data_file_full_paths.append( raw_data_file_full_path)
        # else :
            # we have to download the file. 

    logging.debug(f'Reading data from {len(raw_data_file_full_paths)} files.')

    return raw_data_file_full_paths

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # get_top_20_deliveries('15042021', '13042021')
    # get_top_20_deliveries('15042021')
    get_top_20_deliveries('14042021')
