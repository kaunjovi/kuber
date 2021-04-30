import os
import logging
import pandas as pd 
from util import get_top_delivery_file_name
from util import get_top_average_delivery_file_name
from util import get_sec_bhavdata_file_name
from util import get_top_deliveries_file_quoted_first_step
from util import get_top_deliveries_js_data_file


def generate_js_data_files(date_strings) : 
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

# "SYMBOL","SERIES","DATE1","PREV_CLOSE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","LAST_PRICE","CLOSE_PRICE",
# "AVG_PRICE","TTL_TRD_QNTY","TURNOVER_LACS","NO_OF_TRADES","DELIV_QTY","DELIV_PER","DELIV_LACS"

    big_df.drop('SERIES', axis=1, inplace=True)  
    big_df.drop('OPEN_PRICE', axis=1, inplace=True)  
    big_df.drop('HIGH_PRICE', axis=1, inplace=True)  
    big_df.drop('LOW_PRICE', axis=1, inplace=True)  
    big_df.drop('LAST_PRICE', axis=1, inplace=True)  


    big_df.to_csv(get_top_deliveries_file_quoted_first_step(), index = False, header=True, quoting=1)

    # Using readlines()
    file1 = open(get_top_deliveries_file_quoted_first_step(), 'r')
    lines = file1.readlines()
    lines.pop(0)


    with open(get_top_deliveries_js_data_file(), 'w') as file:
        file.write('var dataSet = [ \n' )
        for line in lines : 
            file.write('[' + line + '] , \n')
        file.write('] \n')

if __name__ == "__main__":
    date_strings = ['05042021']
    generate_js_data_files(date_strings)
