import os
import logging
import pandas as pd 
from constants import get_top_delivery_file_name
from constants import get_top_average_delivery_file_name
from constants import get_sec_bhavdata_file_name
from constants import get_top_deliveries_csv_data_file
from constants import get_top_deliveries_js_data_file


def generate_top_daily_deliveries_csv(date_strings , tag = 'default') : 
    top_delivery_file_names = []
    dfs = []

    for date_string in date_strings : 
        logging.debug(f'date string {date_string}')
        top_delivery_file_name = get_top_delivery_file_name(date_string) 
        if os.path.isfile(top_delivery_file_name) == True :
            logging.debug(f'{top_delivery_file_name} exists.')
            # os.remove(get_top_delivery_file_name(date_string))
            top_delivery_file_names.append(top_delivery_file_name)
            dfs.append(pd.read_csv(top_delivery_file_name))
        else : 
            logging.debug(f'{top_delivery_file_name} does not exist. Moving on.')

    big_df = pd.concat(dfs, ignore_index=True)

# "SYMBOL","SERIES","DATE1","PREV_CLOSE","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","LAST_PRICE","CLOSE_PRICE",
# "AVG_PRICE","TTL_TRD_QNTY","TURNOVER_LACS","NO_OF_TRADES","DELIV_QTY","DELIV_PER","DELIV_LACS"

    big_df.drop('SERIES', axis=1, inplace=True)  
    big_df.drop('OPEN_PRICE', axis=1, inplace=True)  
    big_df.drop('HIGH_PRICE', axis=1, inplace=True)  
    big_df.drop('LOW_PRICE', axis=1, inplace=True)  
    big_df.drop('LAST_PRICE', axis=1, inplace=True)  


    big_df.to_csv(get_top_deliveries_csv_data_file(tag), index = False, header=True, quoting=1)



def generate_top_daily_deliveries_js(date_strings , tag = 'default') : 
    # first step is to create the CSV file. Use the tag
    generate_top_daily_deliveries_csv (date_strings , tag )

    # Now create the js data array 
    # Using readlines()
    file1 = open(get_top_deliveries_csv_data_file(tag), 'r')
    lines = file1.readlines()
    lines.pop(0)


    with open(get_top_deliveries_js_data_file(tag), 'w') as file:
        # file.write('var dataSet = [ \n' )
        count_top = 0 
        file.write('[ \n' )
        for line in lines : 
            if count_top == 0 : 
                count_top += 1 
            else : 
                file.write(' , \n')
            file.write('[' + line + '] ')
        file.write(' \n ]')

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)
#     date_strings = ['05042020']
#     generate_top_daily_deliveries_js(date_strings)
