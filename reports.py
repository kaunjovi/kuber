from datetime import date
import logging
import os.path
import urllib.request
from urllib.error import HTTPError, URLError
from socket import timeout
import shutil
from download_raw_data import get_full_path_of_raw_data_file
from download_raw_data import download_data_for_date_string
import glob
import pandas as pd
import constants

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
    logging.debug(f'Fetching raw file for {len(date_strings)} dates.')

    raw_data_file_full_paths = fetch_raw_data_file_full_paths(date_strings)
    logging.debug(f'Reading data from {len(raw_data_file_full_paths)} files.')

    pd.set_option('display.max_rows', 2000)
    pd.set_option('display.float_format', '{:,.2f}'.format)

    dfs = []
    for filename in raw_data_file_full_paths:
        # dfs.append(pd.read_csv(filename))
        df = pd.read_csv(filename)

        df.rename(columns=lambda x: x.strip(), inplace=True)

        ## DELIV_PER has some '-' in it. Fix them. Fix the column type. 
        df['DELIV_PER'] = df['DELIV_PER'].str.strip()
        df['DELIV_PER'] = df['DELIV_PER'].replace(['-'],'0.00')
        df[['DELIV_PER']] = df[['DELIV_PER']].apply(pd.to_numeric)

        ## DELIV_QTY has some '-' in it. Fix them. Fix the column type. 
        df['DELIV_QTY'] = df['DELIV_QTY'].str.strip()
        df['DELIV_QTY'] = df['DELIV_QTY'].replace(['-'],'0')
        df[['DELIV_QTY']] = df[['DELIV_QTY']].apply(pd.to_numeric)

        ## DELIV_LAC 
        df['DELIV_LACS'] = df.apply (lambda row: (row['AVG_PRICE'] * row['DELIV_QTY'] )/100_000 , axis=1)
        df['DELIV_LACS'] = df['DELIV_LACS'].astype(int)

        ## 
        df['SERIES'] = df['SERIES'].str.strip()

        df = df[df['SERIES']=='EQ']
        df = df.sort_values('DELIV_LACS' , ascending=False)

        print (df.head(20))

        dfs.append(df.head(20))

    big_frame = pd.concat(dfs, ignore_index=True)

    logging.debug(f'Got the big_frame {big_frame.describe()}')

    # print(big_frame)

    return raw_data_file_full_paths , big_frame

if __name__ == "__main__":
# #     # run the code for today.
#     # get_top_20_deliveries()
    files, df = get_top_20_deliveries('15042021', '16042021', '19042021')
    print(df)
#     # logging.basicConfig(level=logging.DEBUG)
#     # get_top_20_deliveries('15042021', '13042021')
#     # get_top_20_deliveries('15042021')
#     # get_top_20_deliveries('15042020')
#     # get_top_20_deliveries('14042021', '15042021', '17042021', '16042021', '18042021' )