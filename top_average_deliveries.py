import os
import logging
import pandas as pd 
from constants import get_top_delivery_file_name
from constants import get_top_average_delivery_file_name
from constants import get_sec_bhavdata_file_name


# ip
# date_strings - the dates for which to calculat the top average deliveris and create file. 
# op 
# row_count - number of rows in the dataset 
# get_top_average_delivery_file_name - name of the file with avg deliveries
def generate_top_average_delivery_file(date_strings) : 

    top_delivery_file_names = []
    dfs = []

    for date_string in date_strings : 
        top_delivery_file_name = get_top_delivery_file_name(date_string) 
        if os.path.isfile(top_delivery_file_name) == True :
            logging.debug(f'{top_delivery_file_name} exists.')
            # os.remove(get_top_delivery_file_name(date_string))
            top_delivery_file_names.append(top_delivery_file_name)
            dfs.append(pd.read_csv(top_delivery_file_name))
        else : 
            logging.debug(f'{top_delivery_file_name} does not exist. Creating one now.')

    big_df = pd.concat(dfs, ignore_index=True)
    df_grouped = big_df.groupby('SYMBOL').agg({'DELIV_LACS': ['mean'], 'SYMBOL': ['count']})
    df_grouped.columns = df_grouped.columns.droplevel(0)
    df_grouped = df_grouped.reset_index() 
    df_sorted_grouped = df_grouped.sort_values(by='mean' , ascending=False)

    # logging.debug(f'{df_sorted_grouped}')

    df_sorted_grouped.to_csv(get_top_average_delivery_file_name(), index = False, header=True)
    # df_sorted_grouped.to_csv(get_top_average_delivery_file_name(), index = False, header=True, quoting=1)
        
    return len(df_sorted_grouped.index), get_top_average_delivery_file_name


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    date_strings = ['05042021','06042021','07042021','08042021','09042021']
    generate_top_average_delivery_file(date_strings)
